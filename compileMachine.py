import os
import subprocess
import sys
from compileMachineMisc import fixPath
from compileMachineMisc import getObjectFiles
from environment import Env
from termcolor import colored

def queueFiles(dir, compileQueue):
    for x in os.listdir(dir):
        if os.path.isdir(fixPath(dir) + x):
            queueFiles(fixPath(dir) + fixPath(x), compileQueue)
            
        if x.endswith(".cpp"):
            compileQueue.append(fixPath(dir) + x)


def compileFiles(compileQueue, env):
    for file in compileQueue:
        print(colored("[quickmake_log] -> Command sent: ", 'yellow') + env.compiler + ' ' + file + ' ' + env.includepath + " -c")
        subprocess.run(env.compiler + ' ' + file + ' ' + env.includepath + " -c")
        
    print(colored("[quickmake_log] -> Command sent: ", 'yellow') + env.compiler + ' ' + getObjectFiles(compileQueue) + ' ' + env.libpath + ' ' + env.cflags + ' ' + env.output)
    subprocess.run(env.compiler + ' ' + getObjectFiles(compileQueue) + ' ' + env.libpath + ' ' + env.cflags + ' ' + env.output)

    print(colored("Compiled!", 'green'))