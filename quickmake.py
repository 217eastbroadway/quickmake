import os
import sys
import subprocess

compileQueue = [];

def isCompilerCompatible():
    return sys.argv[2] == "g++" or sys.argv[2] == "gcc" or sys.argv[2] == "clang"

def fixPath(path):
    if not path.endswith("/") and not path.endswith("\\"):
        return path + '/'
    
    return path

def queueFiles(dir):
    for x in os.listdir(dir):
        if os.path.isdir(x):
            queueFiles(fixPath(dir) + fixPath(x))
            
        if x.endswith(".cpp"):
            compileQueue.append(fixPath(dir) + x)

def getObjectFiles():
    objectQueue = ""

    for file in compileQueue:
        temp = file.split("/")[-1];
        temp = temp[slice(0, len(temp)-4)]
        temp += ".o"
        objectQueue += temp + ' '

    return objectQueue

def compileFiles():
    for file in compileQueue:
        print("[quickmake_log] -> Command sent: " + sys.argv[2] + ' ' + file + ' ' + "-c")
        subprocess.run(sys.argv[2] + ' ' + file + ' ' + "-c")
        
    print(sys.argv[2] + ' ' + getObjectFiles())
    subprocess.run(sys.argv[2] + ' ' + getObjectFiles())

#main():
if len(sys.argv) < 3:
    print("Usage: ./quickmake.py dir compiler")
    quit()

if not isCompilerCompatible():
    print("[quickmake_error] -> Incompatible compiler!")
    quit()

queueFiles(".")
compileFiles();