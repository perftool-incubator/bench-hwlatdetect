# bench-hwlatdetect

Scripts and configuration to run the [hwlatdetect](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/hwlatdetect) hardware latency detector within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework. Detects latency anomalies caused by hardware and firmware (SMIs, NMIs, etc.).

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: defines client scripts and parameter transformations |
| `hwlatdetect-base` | Base setup shared by other scripts |
| `hwlatdetect-client` | Client-side benchmark execution |
| `hwlatdetect-runtime` | Runtime extraction |
| `hwlatdetect-post-process` | Post-processing: parses hwlatdetect output into crucible metrics |
| `workshop.json` | Engine image build: compiles rt-tests from source |
