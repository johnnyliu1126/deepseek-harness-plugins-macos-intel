import {test, after} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {Readable} from 'node:stream';
import {apply as balance} from '../plugins/dsh-balance-monitor/index.js';

const scratch = mkdtempSync(join(tmpdir(), 'dsh-collection-routes-'));
process.env.DSH_HOME = scratch;
const {apply: restart} = await import('../plugins/dsh-restart/index.js');
after(() => rmSync(scratch, {recursive: true}));

function host(apply, account) {
  const routes = new Map();
  apply({webServer: {register: row => routes.set(row.path, row.handler)}, get: () => account});
  return routes;
}
async function call(routes, path, {method = 'GET', origin, body = ''} = {}) {
  const req = Readable.from(body ? [Buffer.from(body)] : []);
  req.method = method;
  req.url = path;
  req.headers = origin ? {origin} : {};
  const result = {status: 200, headers: {}, body: ''};
  const res = {
    writeHead(status, headers) {result.status = status; Object.assign(result.headers, headers);},
    setHeader(key, value) {result.headers[key] = value;},
    end(body = '') {result.body = body;},
  };
  await routes.get(path)(req, res);
  result.json = result.body ? JSON.parse(result.body) : null;
  return result;
}

test('balance rejects a remote origin before querying account data', async () => {
  let queries = 0;
  const routes = host(balance, {getBalance: async () => {queries++;}});
  const result = await call(routes, '/dsh-balance-monitor/state', {origin: 'https://example.org'});
  assert.equal(result.status, 403);
  assert.equal(queries, 0);
});

test('balance returns per-currency totals through the host account seam', async () => {
  const routes = host(balance, {getBalance: async () => ({status: 'ready', value: [{currency: 'CNY', balance: '4'}], bonusWallets: [{currency: 'CNY', balance: '2'}]})});
  const result = await call(routes, '/dsh-balance-monitor/state', {origin: 'http://127.0.0.1:3080'});
  assert.equal(result.json.status, 'ready');
  assert.equal(result.json.wallets[0].total, 6);
  assert.equal(result.headers['Cache-Control'], 'no-store');
});

test('balance preserves signed-out and unsupported statuses without zero amounts', async () => {
  const missing = await call(host(balance), '/dsh-balance-monitor/state');
  assert.equal(missing.json.status, 'unsupported');
  const signedOut = await call(host(balance, {getBalance: async () => null}), '/dsh-balance-monitor/state');
  assert.equal(signedOut.json.status, 'signed-out');
  assert.equal(signedOut.json.wallets, null);
});

test('balance coalesces simultaneous requests instead of querying twice', async () => {
  let queries = 0;
  let release;
  const deferred = new Promise(resolve => {release = resolve;});
  const routes = host(balance, {getBalance: async () => {queries++; return deferred;}});
  const first = call(routes, '/dsh-balance-monitor/state');
  const second = call(routes, '/dsh-balance-monitor/state');
  release({status: 'ready', value: [], bonusWallets: []});
  const results = await Promise.all([first, second]);
  assert.equal(queries, 1);
  assert.ok(results.every(result => result.json.status === 'ready'));
});

test('restart enforces POST and rejects external browser origins', async () => {
  const routes = host(restart);
  assert.equal((await call(routes, '/dsh-restart/restart')).status, 405);
  assert.equal((await call(routes, '/dsh-restart/restart', {method: 'POST', origin: 'https://example.org', body: '{}'})).status, 403);
});

test('restart refuses a non-Desktop Node host and never spawns a restart', async () => {
  const result = await call(host(restart), '/dsh-restart/restart', {method: 'POST', body: '{"dryRun":true}'});
  assert.equal(result.status, 409);
});
