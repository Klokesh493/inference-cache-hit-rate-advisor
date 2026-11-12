# Inference Cache Hit Rate Advisor walkthrough

## Business problem

High inference latency can have different causes. Operators need to decide whether cache misses, traffic, or model latency deserve the first investigation.

## Reproduce the workflow

Run `python3 cache_advisor.py sample_cache.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
ranker: healthy
recommendations: increase_ttl_and_precompute
fraud-score: healthy
```

The sample supplies these fields. `endpoint`, `requests_per_min`, `cache_hit_rate`, `p95_latency_ms`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
