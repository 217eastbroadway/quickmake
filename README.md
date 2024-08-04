# quickmake
An automated build system for C++ projects.

<h1> Why is quickmake better?
Quickmake is able to build your project without needing any unnecessarily long makefiles, saving you time and work!
Quickmake is also cross-platform and easily portable!

<h1> Usage
Quickmake will compile all C++ files in your project without any need for makefiles!\
```$ python3 quickmake.py```

If you wanna specify compiler flags, libraries, etc you'll need to generate and edit the config file, to create such run:\
```$ python3 quickmake.py --createconfig```\

If your quickmake config file isn't named 'makeconfig' you'll need to specify the name of the file:\
```$ python3 quickmake.py fancyconfig.txt```