#!/usr/bin/python3

import os
import shutil
from time import sleep
import fnmatch
from check_if_dir_exists import dir_exists


pathOfDirToLookFor = '/home/z002wydr/Documents/Schulungen/Microconsult/OL-OOPFCPP_AW/Exercises'

while True:
    if dir_exists(pathOfDirToLookFor):
        dirNameToFilter = ['cmake-build-debug', 'cmake-build-release', 'build']
        matches = []
        for root, dirnames, filenames in os.walk(pathOfDirToLookFor):
            for name in dirNameToFilter:
                for dirname in fnmatch.filter(dirnames, name):
                    matches.append(os.path.join(root, dirname))
        for match in matches:
            if os.path.isdir(match):
                shutil.rmtree(match)
    else:
        pathOfDirToLookFor = input('Path to the directory to remove debug stuff: ')
    sleep(10)
