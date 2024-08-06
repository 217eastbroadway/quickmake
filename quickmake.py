import os
import sys
import subprocess
import help
from compileMachine import queueFiles
from compileMachine import compileFiles
from fileHandler import createConfig
from environment import Env
from termcolor import colored

#main():
configFile = "makeconfig"

if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        help.getHelpOut()
        quit()

    elif sys.argv[1] == "--createconfig":
        createConfig()
        quit()

    else:
        configFile = sys.argv[1]

env = Env(configFile)
if not help.isCompilerCompatible(env):
    print(colored("[quickmake_error] -> Incompatible compiler!", 'red'))
    quit()

compileQueue = []
queueFiles(env.directory, compileQueue)
compileFiles(compileQueue, env)