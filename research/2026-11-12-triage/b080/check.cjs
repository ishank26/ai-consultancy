const fs = require('fs');
const d = JSON.parse(fs.readFileSync('output.json','utf8'));
const batch = JSON.parse(fs.readFileSync('batch.json','utf8'));
console.log('valid json, businesses:', d.businesses.length, 'batch:', d.batch);
const got = d.businesses.map(b=>b.ref);
const want = batch.map(b=>b.id);
console.log('order match:', JSON.stringify(got)===JSON.stringify(want));
for (const b of d.businesses){
  const missing = ['name','town','ref','status','website','what_they_do','customers','size_signals','listing','website_review','agent_readiness','operations_signals','top_opportunities','scores','sources'].filter(k=>!(k in b));
  if (missing.length) console.log('MISSING', b.ref, missing);
  if (b.top_opportunities.length>3) console.log('TOO MANY OPPS', b.ref);
  const ar=b.agent_readiness;
  for (const k of ['findable','answerable','bookable']) if (ar[k]<0||ar[k]>3) console.log('bad agent score', b.ref, k);
  for (const k of ['gap_size','ability_to_pay','ease','evidence']) if (!(b.scores[k]>=1&&b.scores[k]<=5)) console.log('bad score', b.ref, k);
  if(!b.scores.reasons) console.log('no reasons', b.ref);
}
console.log('ok');
