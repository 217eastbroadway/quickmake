import os
import subprocess
import sys

def fixPath(path):
    if not path.endswith("/") and not path.endswith("\\"):
        return path + '/'
    
    return path

def queueFiles(dir, compileQueue):
    for x in os.listdir(dir):
        if os.path.isdir(x):
            queueFiles(fixPath(dir) + fixPath(x))
            
        if x.endswith(".cpp"):
            compileQueue.append(fixPath(dir) + x)

def getObjectFiles(compileQueue):
    objectQueue = ""

    for file in compileQueue:
        temp = file.split("/")[-1];
        temp = temp[slice(0, len(temp)-4)]
        temp += ".o"
        objectQueue += temp + ' '

    return objectQueue

def compileFiles(compileQueue):
    for file in compileQueue:
        print("[quickmake_log] -> Command sent: " + sys.argv[2] + ' ' + file + ' ' + "-c")
        subprocess.run(sys.argv[2] + ' ' + file + ' ' + "-c")
        
    print(sys.argv[2] + ' ' + getObjectFiles())
    subprocess.run(sys.argv[2] + ' ' + getObjectFiles())
