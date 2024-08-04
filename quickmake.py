import os
import sys
import subprocess
import help
from queuebuilder import queueFiles
from queuebuilder import compileFiles

#main():
if sys.argv[1] == "--help":
    help.getHelpOut()
    quit()

if len(sys.argv) < 3:
    print("Usage: ./quickmake.py [dir] [compiler]")
    quit()

if not help.isCompilerCompatible():
    print("[quickmake_error] -> Incompatible compiler!")
    quit()


compileQueue = []

queueFiles(".", compileQueue)
compileFiles(compileQueue);