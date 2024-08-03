import os
import sys
import subprocess
import help
from queuebuilder import queueFiles
from queuebuilder import compileFiles

#main():
if len(sys.argv) < 3:
    print("Usage: ./quickmake.py [dir] [compiler]")
    quit()

if not help.isCompilerCompatible():
    print("[quickmake_error] -> Incompatible compiler!")
    quit()

if sys.argv[2] == "--help":
    help.getHelpOut()
    quit()

compileQueue = []

queueFiles(".", compileQueue)
compileFiles(compileQueue);