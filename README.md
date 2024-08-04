# quickmake
An automated build system for C++ projects.

# Why is quickmake better?
Quickmake is able to build your project without needing any unnecessarily long makefiles, saving you time and work!
Quickmake is also cross-platform and easily portable!

# Usage
Quickmake will compile all C++ files in your project without any need for makefiles!
```$ python3 quickmake.py```

If you wanna specify compiler flags, libraries, etc you'll only need to run:
```$ python3 quickmake.py --createconfig```
You'll then be able to edit the 'makeconfig' files with all the tweaks you might need!

If your quickmake config file isn't named 'makeconfig' you'll need to specify the name of the file:
```$ python3 quickmake.py fancyconfig.txt```