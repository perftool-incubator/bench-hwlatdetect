#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import argparse
import json
import os
import re
import sys
from pathlib import Path

TOOLBOX_HOME = os.environ.get("TOOLBOX_HOME")
if TOOLBOX_HOME:
    sys.path.append(str(Path(TOOLBOX_HOME) / "python"))

from toolbox.cdm_metrics import CDMMetrics


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--duration", default=None)
    parser.add_argument("--threshold", default=None)
    parser.parse_known_args()

    primary_metric = "latency-spikes-usec"

    times = {}
    for name in ("begin", "end"):
        with open(f"{name}.txt") as f:
            times[name] = int(float(f.read().strip()) * 1000)

    result_file = "hwlatdetect-bin-stderrout.txt"
    if not os.path.exists(result_file):
        return

    metrics = CDMMetrics()
    latency_threshold = None

    with open(result_file) as f:
        for line in f:
            m = re.search(r"Latency threshold:\s+(\d+)us", line)
            if m:
                latency_threshold = int(m.group(1))
                continue

            m = re.search(r"Max Latency:\s+(.*)$", line)
            if m:
                result = m.group(1)
                max_latency = -1

                if "Below threshold" in result:
                    max_latency = latency_threshold
                else:
                    m2 = re.search(r"(\d+)us", result)
                    if m2:
                        max_latency = int(m2.group(1))

                if max_latency == -1:
                    print("ERROR: Failed to determine max latency, something unexpected probably happened!")
                    sys.exit(1)

                desc = {"source": "hwlatdetect", "type": primary_metric, "class": "count"}
                sample = {"begin": times["begin"], "end": times["end"], "value": max_latency}
                metrics.log_sample("0", desc, {}, sample)

    metric_data_name = metrics.finish_samples()

    if metric_data_name:
        sample_data = {
            "rickshaw-bench-metric": {"schema": {"version": "2021.04.12"}},
            "benchmark": "hwlatdetect",
            "primary-period": "measurement",
            "primary-metric": primary_metric,
            "periods": [
                {
                    "name": "measurement",
                    "metric-files": [metric_data_name],
                }
            ],
        }

        with open("post-process-data.json", "w") as f:
            json.dump(sample_data, f)


if __name__ == "__main__":
    main()
