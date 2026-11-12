# Inference Cache Hit Rate Advisor

Recommends cache tuning actions for model-serving endpoints based on hit rate, latency, and traffic volume.

Focus: inference platform, latency SLOs, cache reliability, AI serving cost.

Portfolio framing: Apple-scale client-style AI platform project using synthetic data only.

## Run

```bash
python3 cache_advisor.py sample_cache.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

High inference latency can have different causes. Operators need to decide whether cache misses, traffic, or model latency deserve the first investigation.

## Project walkthrough

```mermaid
flowchart LR
    A["Endpoint cache and latency metrics"]
    B["Evaluate hit rate, latency, and traffic volume"]
    C{"Which ordered policy matches?"}
    D["Recommend TTL, warm keys, or profiling"]
    E["Keep current settings if none match"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 cache_advisor.py sample_cache.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
