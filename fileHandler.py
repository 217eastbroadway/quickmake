import os

def generateConfigFile():
    f = open("makeconfig", "w")
    f.write("directory = #Set your project directory here.\ncompiler = #Set your compiler here, the default compiler is g++.\ncflags = #Set your compiler flags here.\noutput = #Set the output name of your project here (eg: app.exe)\nincludepath = #Set the path to include files your project might need\nlibpath = #Set the path to library files your project might need")
    f.close()


def createConfig():
    if os.path.exists("makeconfig"):
        if input("[quickmake_warning] -> Quickmake configuration already exists! Do you want to overwrite it? [Y/N]\n> ").lower() == 'y':
            generateConfigFile()
    else:
        generateConfigFile()

def getConfigData(configfile):
    f = open(configfile, "r")
    
    configData = []
    for line in f:
        configData.append(line.replace('\n', ''))

    return configData