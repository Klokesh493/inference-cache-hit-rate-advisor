import csv
import sys


def recommendation(row):
    hit_rate = float(row["cache_hit_rate"])
    latency = float(row["p95_latency_ms"])
    rpm = int(row["requests_per_min"])
    if hit_rate < 0.60 and latency > 250:
        return "increase_ttl_and_precompute"
    if hit_rate < 0.75 and rpm > 5000:
        return "expand_warm_keys"
    if latency > 250:
        return "profile_model_latency"
    return "healthy"


def advise(rows):
    return [{"endpoint": row["endpoint"], "recommendation": recommendation(row)} for row in rows]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in advise(csv.DictReader(handle)):
            print(f'{item["endpoint"]}: {item["recommendation"]}')


if __name__ == "__main__":
    main(sys.argv[1])
