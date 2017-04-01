#!/usr/bin/python3.5

import os

dirName = input("What would you like to name your directory? ")

pathName = input("Enter path for your new directory (do not enter new directory name): ")

testString = []

for i in pathName:
    testString.append(i)

if testString[-1] == '/':
    newDirectoryPath = "'mkdir {}{}'".format(pathName, dirName)

else:
    newDirectoryPath = "'mkdir {}/{}'".format(pathName, dirName)
    
print(newDirectoryPath)
#os.system(newDirectoryPath)
