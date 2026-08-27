# Bench-hwlatdetect

## Purpose
Scripts and configuration to run the hwlatdetect hardware latency detector within the crucible framework. Detects latency anomalies caused by hardware and firmware (SMIs, NMIs, etc.).

## Language
- Bash for benchmark execution scripts
- Python for post-processing (`hwlatdetect-post-process.py`)

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client scripts, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `hwlatdetect-base` | Base setup shared by other scripts |
| `hwlatdetect-client` | Client-side benchmark execution |
| `hwlatdetect-runtime` | Extracts runtime from command-line options |
| `hwlatdetect-post-process.py` | Parses hwlatdetect output into crucible metrics |
| `workshop.json` | Engine image build: compiles rt-tests from source |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
- Python code follows 4-space indentation with standard modelines
