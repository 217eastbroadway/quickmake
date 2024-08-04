import os
import subprocess
import sys
from compileMachineMisc import fixPath
from compileMachineMisc import getObjectFiles
    
def queueFiles(dir, compileQueue):
    for x in os.listdir(dir):
        if os.path.isdir(x):
            queueFiles(fixPath(dir) + fixPath(x))
            
        if x.endswith(".cpp"):
            compileQueue.append(fixPath(dir) + x)


def compileFiles(compileQueue):
    for file in compileQueue:
        print("[quickmake_log] -> Command sent: " + sys.argv[2] + ' ' + file + ' ' + "-c")
        subprocess.run(sys.argv[2] + ' ' + file + ' ' + "-c")
        
    print(sys.argv[2] + ' ' + getObjectFiles())
    subprocess.run(sys.argv[2] + ' ' + getObjectFiles())
