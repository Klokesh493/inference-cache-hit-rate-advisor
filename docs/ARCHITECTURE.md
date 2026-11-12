# Inference Cache Hit Rate Advisor architecture

Recommends cache tuning actions for model-serving endpoints based on hit rate, latency, and traffic volume.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
