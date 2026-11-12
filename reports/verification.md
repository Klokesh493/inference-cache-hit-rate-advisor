# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 cache_advisor.py sample_cache.csv
ranker: healthy
recommendations: increase_ttl_and_precompute
fraud-score: healthy
test_precompute_for_low_hit_rate_and_high_latency (test_cache_advisor.CacheAdvisorTest) ... ok
test_reports_endpoint_recommendation (test_cache_advisor.CacheAdvisorTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
