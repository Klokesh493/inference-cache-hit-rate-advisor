import unittest

from cache_advisor import advise, recommendation


class CacheAdvisorTest(unittest.TestCase):
    def test_precompute_for_low_hit_rate_and_high_latency(self):
        row = {"cache_hit_rate": "0.52", "p95_latency_ms": "310", "requests_per_min": "14000"}
        self.assertEqual(recommendation(row), "increase_ttl_and_precompute")

    def test_reports_endpoint_recommendation(self):
        rows = [{"endpoint": "ranker", "cache_hit_rate": "0.86", "p95_latency_ms": "115", "requests_per_min": "9000"}]
        self.assertEqual(advise(rows)[0]["recommendation"], "healthy")


if __name__ == "__main__":
    unittest.main()
