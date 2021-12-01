# Controlling CNC machines with python

This simple implementation is an example of how to contol CNC machines running GRBL with python 

This script converts the supplied .gcode into movement without the use of a dedicated controlling application (e.g. CNCjs, OpenbuildsCONTROL, etc)

I built this becuase a lot of the documentation for sending a stream of gcode to a grbl controller was written in python2 and no longer worked
Additionally, many of the implementations did not buffer or wait for commands to finish before going onto the next

---------------------------------------------------------------

How to use

run:
```
  python simple_stream.py
```

---------------------------------------------------------------

tested on
> MacOs (M1 Monterey arm64)
> Python 3.9.5 | packaged by conda-forge | (default, Jun 19 2021, 00:24:55) [Clang 11.1.0 ] on darwin
> Vscode 1.62.3
> Openbuilds BlackBox GRBL controller
> GRBL 1.1
