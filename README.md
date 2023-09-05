# Controlling GRBL/CNC/gcode machines with python or MATLAB

This simple implementation is an example of how to contol CNC machines running GRBL with python 

This script converts the supplied .gcode into movement without the use of a dedicated controlling application (e.g. CNCjs, OpenbuildsCONTROL, etc)

I built this becuase a lot of the documentation for sending a stream of gcode to a grbl controller was written in python2 and no longer worked with python3 syntax. Additionally, many of the implementations did not buffer or wait for commands to finish before going onto the next, my script is an attempt to fix these issues

All tweaking and setup of the grbl controller should be done in an outside program (I recommend CNCjs), all this script does is read grbl_test.gcode and feeds each individual line to the grbl controller, waits for completion of said line, and then moves onto the next line of gcode.

---------------------------------------------------------------

# How to use:

install python prerequisites 
```
  python -m pip install pyserial
```

You most likely will have to change the COM port in `simple_stream.py` (or .m) to the associated port (Correct port can be found in an external CNC control software ex. CNCjs).

Note: Linux/Max COM ports have a different name and path type than windows com ports



## run:
```
  python simple_stream.py
```

---------------------------------------------------------------

tested on:

```
MacOs (M1 Monterey arm64)
Python 3.9.5 | packaged by conda-forge | (default, Jun 19 2021, 00:24:55) [Clang 11.1.0 ] on darwin
Vscode 1.62.3
Openbuilds BlackBox GRBL controller
GRBL 1.1
```

![Alt Text](https://github.com/Sam-Freitas/python_to_GRBL/blob/main/readme_deps/9EC680F1-AE1E-4AD0-9828-93B54D571714%20(1).gif)
