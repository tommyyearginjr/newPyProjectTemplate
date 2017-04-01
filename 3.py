#!/usr/bin/python3.5

import os



dirName = input("What would you like to name your directory? ")

pathName = input("Enter path for your new directory (do not enter new directory name): ")

testString = []

for i in pathName:
    testString.append(i)

if testString[-1] == '/':
    newDirectoryPath = "{}{}".format(pathName, dirName)
    createDirectory = "'mkdir {}; cd {}'".format(newDirectoryPath, newDirectoryPath)

else:
    newDirectoryPath = "{}/{}".format(pathName, dirName)
    createDirectory = "'mkdir {}; cd {}'".format(newDirectoryPath, newDirectoryPath)
    
#print(createDirectory)


finish = 'touch 1.py 2.py 3.py 4.py 5.py README.md LICENSE.txt; chmod +x *.py; git init; git add *;\
 git commit -m "commit"; clear; git status'

#print(finish)

os.system(createDirectory)
os.system(finish)
