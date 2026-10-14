#!/usr/bin/env python3
"""Prepare the approved local review workflow in native cloud workspace storage."""
from pathlib import Path,PurePosixPath
import hashlib,json,subprocess,sys,zipfile
repo=Path(__file__).resolve().parents[1];meta=json.loads((repo/'cloud-environment/SOURCE.json').read_text());archive=repo/'downloads'/meta['file'];digest=hashlib.sha256(archive.read_bytes()).hexdigest()
if digest!=meta['sha256']:raise SystemExit('Release archive integrity mismatch; existing work was preserved')
target=Path('/workspace')/('idigitalroot-cloud-operator-'+digest[:20])
if not target.exists():
 with zipfile.ZipFile(archive) as z:
  if z.testzip():raise SystemExit('Release archive CRC mismatch')
  if len(z.infolist())>5000 or sum(i.file_size for i in z.infolist())>100*1024*1024:raise SystemExit('Unexpected archive limits')
  for i in z.infolist():
   p=PurePosixPath(i.filename)
   if p.is_absolute() or '..' in p.parts or '\\' in i.filename or ((i.external_attr>>16)&0o170000)==0o120000:raise SystemExit('Unsafe archive entry')
  target.mkdir();z.extractall(target)
subprocess.run(['sha256sum','--check','SHA256SUMS.txt'],cwd=target,check=True,stdout=subprocess.DEVNULL)
cmd=[sys.executable,'-u',str(target/'OPEN_CONNECTED_PREVIEW.py'),'--no-open','--state-root','/workspace/idigitalroot-connected-runtime','--test-seconds','2']
for flag,version in [('--frontend-node','22.19.0'),('--backend-node','22.16.0')]:
 node=Path('/workspace/idigitalroot-tools')/f'node-v{version}-linux-x64/bin/node'
 if node.exists():cmd.extend([flag,str(node)])
subprocess.run(cmd,cwd=target,check=True)
(repo/'cloud-environment/LOCAL_READY.json').write_text(json.dumps({'operator':str(target),'sourceArchiveSha256':digest,'providerMutation':False,'deployment':False},indent=2)+'\n')
print('SETUP_PASS: real local Workers/D1/R2 and connected public website start/stop verified; owner data and provider resources unchanged')
