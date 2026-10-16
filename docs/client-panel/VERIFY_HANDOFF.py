#!/usr/bin/env python3
"""Read-only integrity verification. Does not install, extract, run source or contact a provider."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,io,json,re,zipfile

def safe(name):
 p=PurePosixPath(name)
 if not name or p.is_absolute()or '..'in p.parts or '\\'in name or ':'in p.parts[0]:raise ValueError('Unsafe archive/manifest path')
 return name

def verify(reader,names):
 manifest=json.loads(reader('RELEASE_MANIFEST.json'));files=manifest['files'];expected={}
 for row in files:
  name=safe(row['path'])
  if name in expected:raise ValueError('Duplicate manifest entry')
  raw=reader(name)
  if hashlib.sha256(raw).hexdigest()!=row['sha256']or len(raw)!=row['size_bytes']:raise ValueError('Manifest content mismatch: '+name)
  expected[name]=row['sha256']
 checks={}
 for line in reader('SHA256SUMS.txt').decode().splitlines():
  digest,name=line.split('  ',1);safe(name)
  if not re.fullmatch('[a-f0-9]{64}',digest)or name in checks:raise ValueError('Invalid checksum entry')
  if hashlib.sha256(reader(name)).hexdigest()!=digest:raise ValueError('Checksum mismatch: '+name)
  checks[name]=digest
 if set(checks)!=set(expected)|{'RELEASE_MANIFEST.json'}:raise ValueError('Manifest/checksum coverage mismatch')
 if set(names)!=set(expected)|{'RELEASE_MANIFEST.json','SHA256SUMS.txt'}:raise ValueError('Unexpected/missing handoff files; preserve originals and inspect differences')
 # The sealed source stays an immutable nested ZIP. Check all of its recorded file bytes too.
 sources=json.loads(reader('SOURCES_AND_AUTHORITY.json'));source=sources['currentPublicCmsSource'];path=source['bundledInSmallZipAt'];raw=reader(path)
 if hashlib.sha256(raw).hexdigest()!=source['sha256']:raise ValueError('Current source SHA mismatch')
 with zipfile.ZipFile(io.BytesIO(raw))as z:
  if z.testzip():raise ValueError('Current source CRC mismatch')
  for line in z.read('SHA256SUMS.txt').decode().splitlines():
   h,n=line.split('  ',1);safe(n)
   if hashlib.sha256(z.read(n)).hexdigest()!=h:raise ValueError('Current source file checksum mismatch')
 return {'status':'PASS_HANDOFF_INTEGRITY_ONLY','handoff':manifest['handoff'],'files':len(files),'currentPublicSourceSha256':source['sha256'],'clientImplementation':'NOT_BUILT','clientSecurityAssessment':'NOT_ASSESSED_CLIENT_PANEL','deployment':False}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--zip',type=Path);p.add_argument('--master',type=Path);a=p.parse_args()
 if a.zip:
  if a.zip.stat().st_size>32*1024*1024:raise ValueError('Unexpected small-handoff archive size')
  with zipfile.ZipFile(a.zip)as z:
   entries=z.infolist();names=[safe(i.filename)for i in entries if not i.is_dir()]
   if len(names)!=len(set(names))or len(entries)>2000 or sum(i.file_size for i in entries)>64*1024*1024:raise ValueError('Unexpected archive layout/limits')
   if any(((i.external_attr>>16)&0o170000)==0o120000 for i in entries):raise ValueError('Archive symlink')
   if z.testzip():raise ValueError('ZIP CRC mismatch')
   result=verify(z.read,names)
 else:
  root=Path(__file__).resolve().parent
  def reader(name):
   target=root/safe(name)
   if target.is_symlink()or not target.resolve().is_relative_to(root):raise ValueError('Escaping/symlink handoff file')
   return target.read_bytes()
  names=[]
  for target in root.rglob('*'):
   if '__pycache__'in target.relative_to(root).parts:continue
   if target.is_symlink():raise ValueError('Handoff symlink')
   if target.is_file():names.append(str(target.relative_to(root)))
  result=verify(reader,names)
 if a.master:
  raw=a.master.read_bytes();expected='f1ea6c341baf3c81afa5b797ed09beb9b1a400325338e8a42ed671c2a5f23b20'
  if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('Original master SHA mismatch')
  with zipfile.ZipFile(io.BytesIO(raw))as z:
   if z.testzip():raise ValueError('Original master CRC mismatch')
   for line in z.read('SHA256SUMS.txt').decode().splitlines():
    h,n=line.split('  ',1);safe(n)
    if hashlib.sha256(z.read(n)).hexdigest()!=h:raise ValueError('Original master checksum mismatch')
   for row in json.loads(z.read('RELEASE_MANIFEST.json'))['files']:
    if hashlib.sha256(z.read(safe(row['path']))).hexdigest()!=row['sha256']:raise ValueError('Original master manifest mismatch')
  result['masterCompanion']='PASS_SHA_CRC_MANIFEST_CHECKSUMS'
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
