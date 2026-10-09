# Validation Report

**Suite:** JA21 DeepML Kernel Language Suite 1.0.0  
**Result:** **PASS**  
**Validation mode:** Structural, catalog, provenance-field, policy-envelope, and package-integrity validation

## Results

| Check | Result |
|---|---:|
| Uploaded wrapper records decoded | 7 |
| Normalized technical records | 10,000 |
| Unique technical record IDs | 10,000 |
| Curated `.dmk` scripts | 1,000 |
| Unique curated record IDs | 1,000 |
| Script catalog rows | 1,000 |
| Feature vocabulary | 31 |
| Proficiency levels represented | 10 |
| Validation classes represented | 10 |
| Required program-envelope failures | 0 |
| Brace-balance failures | 0 |
| Source-hash failures | 0 |
| Maximum relative path length | 80 characters |

## Distribution check

The 1,000-script pack preserves exactly one tenth of the full corpus validation-class distribution: 400 positive, 150 negative, 100 boundary, 100 integration, 75 security, 50 performance, 50 determinism, 25 interoperability, 25 recovery, and 25 certification examples. It also includes exactly 100 scripts from each proficiency level.

## What this report does not establish

No production DeepML Kernel compiler or JA21 device runtime was supplied. Therefore this report does not establish native parsing, type checking, lowering, device execution, numerical correctness, performance, security certification, or scientific validity of the Smithson 8S Coupled Mechanics model. Corpus `expected_status` values remain specifications marked `modeled_not_executed`.

## Reproduction

Run from the suite root:

```bash
python tools/validate_suite.py
```

All structural publication gates passed.
