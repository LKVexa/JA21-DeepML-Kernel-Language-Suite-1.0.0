#!/usr/bin/env python3
"""Offline inspector for JA21 DMK technical corpus."""
import argparse, gzip, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
CORPUS=ROOT/'corpus/technical/JA21_DMK_TECHNICAL_CORPUS_10000.jsonl.gz'
p=argparse.ArgumentParser(); p.add_argument('--record'); p.add_argument('--feature'); p.add_argument('--level'); p.add_argument('--class-name'); p.add_argument('--limit',type=int,default=20)
a=p.parse_args(); shown=0
with gzip.open(CORPUS,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        if a.record and r['record_id']!=a.record: continue
        if a.feature and r['feature']!=a.feature: continue
        if a.level and r['level']!=a.level: continue
        if a.class_name and r['validation_class']!=a.class_name: continue
        print(json.dumps(r,indent=2,ensure_ascii=False)); shown+=1
        if shown>=a.limit: break
if shown==0: sys.exit('No matching records.')
