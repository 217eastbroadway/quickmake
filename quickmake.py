import os
import sys
import subprocess
import help
from compileMachine import queueFiles
from compileMachine import compileFiles
from fileHandler import createConfig
#main():
if sys.argv[1] == "--help":
    help.getHelpOut()
    quit()

if sys.argv[1] == "--createconfig":
    createConfig()

if len(sys.argv) < 3:
    print("Usage: ./quickmake.py [dir] [compiler]")
    quit()

if not help.isCompilerCompatible():
    print("[quickmake_error] -> Incompatible compiler!")
    quit()


compileQueue = []

queueFiles(".", compileQueue)
compileFiles(compileQueue);