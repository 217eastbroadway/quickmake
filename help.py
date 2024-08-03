import sys

def getHelpOut():
    print("[quickmake_help] -> ./quickmake [dir] [compiler] [includepath/includefiles] [libpath/libs]")

def isCompilerCompatible():
    return sys.argv[2] == "g++" or sys.argv[2] == "gcc" or sys.argv[2] == "clang"