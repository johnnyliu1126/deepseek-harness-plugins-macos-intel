import {pricing,normalize} from './core.js';
export const name='dsh-balance-monitor';
export const inject=['webServer'];
export function apply(ctx){let pending=null,lastRequest=0;
ctx.webServer.register({kind:'exact',path:'/dsh-balance-monitor/state',handler:async(req,res)=>{
const origin=req.headers.origin;if(origin&&origin!=='null'&&!/^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin)){res.writeHead(403);res.end();return;}
res.setHeader('Cache-Control','no-store');res.setHeader('Content-Type','application/json');
const account=ctx.get('deepseekAccount');
try{if(!account){res.end(JSON.stringify({status:'unsupported',pricing:pricing()}));return;}
if(!pending&&Date.now()-lastRequest>3000){lastRequest=Date.now();pending=(async()=>{const b=await account.getBalance({version:process.env.DSH_CLIENT_VERSION||'0.2.1',locale:'zh-CN',timezoneOffsetSeconds:28800});return {status:b===null?'signed-out':b.status==='ready'?'ready':'failed',wallets:normalize(b),updatedAt:Date.now()};})();pending.finally(()=>{pending=null}).catch(()=>{});}
const data=pending?await pending:{status:'throttled'};res.end(JSON.stringify({...data,pricing:pricing()}));
}catch{res.end(JSON.stringify({status:'failed',pricing:pricing()}));}
}});}
