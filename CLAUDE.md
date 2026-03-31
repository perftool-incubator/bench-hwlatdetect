# Bench-hwlatdetect

## Purpose
Scripts and configuration to run the hwlatdetect hardware latency detector within the crucible framework. Detects latency anomalies caused by hardware and firmware (SMIs, NMIs, etc.).

## Language
Bash — all scripts

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client scripts, parameter transformations |
| `hwlatdetect-base` | Base setup shared by other scripts |
| `hwlatdetect-client` | Client-side benchmark execution |
| `hwlatdetect-runtime` | Extracts runtime from command-line options |
| `hwlatdetect-post-process` | Parses hwlatdetect output into crucible metrics |
| `workshop.json` | Engine image build: compiles rt-tests from source |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
