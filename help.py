import sys
from environment import Env

def getHelpOut():
    print("[quickmake_help] -> ./quickmake [quickmakeconfigurationfile]")

def isCompilerCompatible(env):
    return "g++" in env.compiler or "gcc" in env.compiler or "clang" in env.compiler