#!/usr/bin/python3.5

import os

dirName = input("What would you like to name your directory? ")

pathName = input("Enter complete directory path for your new directory: ")

newDirectoryPath = "'mkdir {}{}'".format(pathName, dirName)

print(newDirectoryPath)
#os.system(newDirectoryPath)
