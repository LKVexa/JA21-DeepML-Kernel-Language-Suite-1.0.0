#!/usr/bin/env python3
"""Structural validator for JA21 DeepML Kernel Language Suite 1.0.0."""
import csv,gzip,json,pathlib,hashlib,sys,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[]
corpus=ROOT/'corpus/technical/JA21_DMK_TECHNICAL_CORPUS_10000.jsonl.gz'
ids=set(); n=0
with gzip.open(corpus,'rt',encoding='utf-8') as f:
    for line in f:
        n+=1
        try:r=json.loads(line)
        except Exception as e: errors.append(f'corpus line {n}: {e}');continue
        rid=r.get('record_id')
        if rid in ids: errors.append(f'duplicate record id: {rid}')
        ids.add(rid)
        for key in ['source','semantic_interpretation','ast','compiler_representation','runtime_representation','validation_result']:
            if key not in r: errors.append(f'{rid}: missing {key}')
if n!=10000: errors.append(f'expected 10000 records, found {n}')
scripts=list((ROOT/'scripts').rglob('*.dmk'))
if len(scripts)!=1000: errors.append(f'expected 1000 scripts, found {len(scripts)}')
with (ROOT/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
if len(rows)!=1000: errors.append(f'expected 1000 script catalog rows, found {len(rows)}')
for row in rows:
    p=ROOT/row['script_path']
    if not p.exists(): errors.append(f'missing script: {row["script_path"]}'); continue
    text=p.read_text(encoding='utf-8')
    required=['ja source 0.3','module ','use DeepMLKernel','policy no_network','kernel ','determinism ','verify bounds','assert kernel.race_free','emit kernel']
    for token in required:
        if token not in text: errors.append(f'{row["record_id"]}: missing token {token!r}')
    if text.count('{')!=text.count('}'): errors.append(f'{row["record_id"]}: unbalanced braces')
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=row['source_sha256']: errors.append(f'{row["record_id"]}: hash mismatch')
maxpath=max(len(str(p.relative_to(ROOT))) for p in ROOT.rglob('*'))
if maxpath>180: errors.append(f'max relative path exceeds 180: {maxpath}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(json.dumps({'status':'PASS','technical_records':n,'unique_record_ids':len(ids),'scripts':len(scripts),'catalog_rows':len(rows),'max_relative_path':maxpath},indent=2))
