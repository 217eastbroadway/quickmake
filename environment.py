import os
import sys
from fileHandler import getConfigData

class Env:
    directory = "."
    compiler = "g++"
    cflags = ""
    output = ""
    includepath = ""
    libpath = ""

    def __init__(self, configfile):
        configData = getConfigData(configfile)
        for configuration in configData:
            if "directory" in configuration:
                if len(configuration.split("=")[1].strip()) > 0:
                    self.directory = configuration.split("=")[1].strip()
            
            if "compiler" in configuration:
                self.compiler = configuration.split("=")[1]
                if " " in self.compiler:
                    self.compiler = self.compiler.split(" ")[1]

            if "cflags" in configuration:
                self.cflags = configuration.split("=")[1]

            if "output" in configuration:
                self.output = "-o " + configuration.split("=")[1]
                
            if "includepath" in configuration:
                temp = configuration.split("=")[1].strip()
                if len(temp) > 0:
                    temp = temp.split(" ")
                    for include in temp:
                        self.includepath += "-I" + include + ' '

            if "libpath" in configuration:
                temp = configuration.split("=")[1].strip()
                if len(temp) > 0:
                    temp = temp.split(" ")
                    for lib in temp:
                        self.libpath += "-L" + lib + ' '