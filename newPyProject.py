#!/usr/bin/python3.5

import os

dirName = input("What would you like to name your directory? ")

pathName = input("Enter path for your new directory (do not enter new directory name): ")

testString = []

for i in pathName:
    testString.append(i)

if testString[-1] == '/':
    newDirectoryPath = "{}{}".format(pathName, dirName)
    createDirectory = "mkdir {}".format(newDirectoryPath)

else:
    newDirectoryPath = "{}/{}".format(pathName, dirName)
    createDirectory = "mkdir {}".format(newDirectoryPath)


finish = "touch {}/3.py {}/2.py {}/4.py {}/5.py {}/1.py {}/README.md {}/LICENSE.txt; chmod +x {}/*.py".format(newDirectoryPath, newDirectoryPath, newDirectoryPath,
                                                                                           newDirectoryPath, newDirectoryPath, newDirectoryPath,
                                                                                                              newDirectoryPath, newDirectoryPath)

os.system('{}'.format(createDirectory))
os.system('{}'.format(finish))

