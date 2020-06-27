# Rainbow Print

Inspired by Rainbow CSV - **Rainbow Print** adds colors to the standard outputs to ease the process of monitoring respective data / metrics

## Main features

* Highlights data points in different colors to ease monitoring capabilities
* By default provides 7 colors (light and dark each) for N Variables(rolling). Supports N colors 
* Support for Dark and Light backgrounds
* Supports string print based on separator / dictionary's key-value based print
* Supports custom colors based on ``sty.fg`` package

## Demo 

How rainbow print helps

### Default print a dictionary of metrics for 10 steps
![Dict Print](https://github.com/kingspp/rainbow-print/blob/master/assets/print_dict.png?raw=true)
### Default print a string of metrics for 10 steps
![Str Print](https://github.com/kingspp/rainbow-print/blob/master/assets/print_str.png?raw=true)
### Rainbow Print - Dark Mode
![Rainbow Print Dark](https://github.com/kingspp/rainbow-print/blob/master/assets/printr-dark.png?raw=true)
### Rainbow Print - Light Mode
![Rainbow Print Light](https://github.com/kingspp/rainbow-print/blob/master/assets/printr-light.png?raw=true)

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
printr(data)

# Get information regarding current configuration
printr.info()
>>Theme: dark
>>Colors: ['\x1b[38;2;5;152;154m', '\x1b[38;2;116;162;103m', '\x1b[38;2;179;128;168m', '\x1b[38;2;255;127;0m', '\x1b[38;2;112;154;180m', '\x1b[38;2;255;255;0m', '\x1b[38;2;255;0;0m']
```

## Configuration
```python
# By default printr works in dark mode
from rainbow_print import printr

# Switch to light palette
printr.set_light_palette()

# Switch to dark palette
printr.set_dark_palette()

# Set colors for dark palette
colors = [sty.fg(0,0,0), sty.fg(255,255,255)]
printr.update_dark_palette(colors)

# Set colors for light palette
colors = [sty.fg(0,0,0), sty.fg(255,255,255)]
printr.update_light_palette(colors)

```
