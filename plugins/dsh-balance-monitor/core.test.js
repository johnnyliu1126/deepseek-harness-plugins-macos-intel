import {test} from 'node:test';
import assert from 'node:assert/strict';
import {pricing,normalize} from './core.js';
test('pricing boundaries and holiday/weekend',()=>{for(const [d,p] of [['2026-11-05T08:59:59+08:00',false],['2026-11-05T09:00:00+08:00',true],['2026-11-05T12:00:00+08:00',false],['2026-11-05T14:00:00+08:00',true],['2026-11-05T18:00:00+08:00',false],['2026-10-01T10:00:00+08:00',false],['2026-10-10T10:00:00+08:00',false]])assert.equal(pricing(Date.parse(d)).peak,p);});
test('wallet currencies remain separate',()=>assert.deepEqual(normalize({status:'ready',value:[{currency:'CNY',balance:'10'}],bonusWallets:[{currency:'CNY',balance:'2'}]}),[{currency:'CNY',recharge:10,bonus:2,total:12}]));
test('failed balance is never zero',()=>assert.equal(normalize({status:'failed'}),null));
