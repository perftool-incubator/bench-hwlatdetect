# bench-hwlatdetect

Benchmark wrapper for hwlat_detector tracer.

## Documentation
https://www.kernel.org/doc/html/latest/trace/hwlat_detector.html

## Source
https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git

## Usage
To start hwlatdetect with the default python utility, run:
```
hwlatdetect-client --duration 60 --threshold 1us
```

To start hwlatdetect with the manual tracer (without the utility), run:
```
hwlatdetect-client --duration 60 --threshold 1us --utility no
```

To start hwlatdetect with custom cpumask and width, run:
```
hwlatdetect-client --duration 60 --threshold 1us --utility no --width 950000 --cpumask ff,ffffffcf,fffffffc
```
Note: cpumask and width are not currently supported by the utility.



