# borehole-analysis

A Python script that reads SPT (Standard Penetration Test) data from a borehole log and produces a summary report.

## What it does

- Reads a borehole log file with depth (m) and SPT blow count per measurement
- Prints each measurement
- Calculates the number of measurements, the average blow count, and the depth of the maximum blow count
- Skips malformed lines instead of crashing, and reports a clear message if the data file is missing

## Data format

`borehole.txt` contains one measurement per line: depth in meters, then blow count, separated by a comma.

```
1.5,4
3.0,7
4.5,12
```

## How to run

Place `borehole.txt` in the same folder as the script, then run:

```
python borehole_safe.py
```

## Example output

```
Depth 1.5 m: 4 blows
Depth 3.0 m: 7 blows
...
Measurements: 6
Average blows: 14.2
Max blows: 31 at 9.0 m
```

## Skills demonstrated

Python file reading, string parsing, loops and conditionals, accumulation and max tracking, error handling with `try`/`except`.

## About

Built by Tal Valevi, an engineering geologist (B.Sc., Ben-Gurion University of the Negev) learning Python and geospatial data analysis on the way to remote sensing.
