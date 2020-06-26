# Rainbow Print

Inspired by Rainbow CSV - **Rainbow Print** adds colors to the standard outputs to ease the process of monitoring respective data / metrics

## Main features

* Highlights data points in different colors to ease monitoring capabilities
* By default provides 7 colors (rolling) for N Variables. User can provide N colors 
* Support for Dark and Light backgrounds
* Supports string print based on separator / dictionary key-value based print
* Supports custom colors based on ``sty`` package

## Demo 

How rainbow print helps

### Default print a dictionary of metrics for 10 steps

### Default print a string of metrics for 10 steps

### Rainbow Print - Dark Mode

### Rainbow Print - Light Mode

## Requirements
1. python >3
2. sty

## Installation
```bash
pip install rainbow-print
```

## Usage
```python
from rainbow_print import printr
data = {"Episode": 10, "Episode Len":5, "Cost": 0.95, "Reward":135, "Mode":"Explore"}
```

## Configuration

