#!/usr/bin/python3

import os
import shutil
import fnmatch
from check_if_dir_exists import dir_exists

pathOfDirToLookFor = r'C:\Users\SW\Desktop\MicroConsult\Clean Code\Uebungen'


def remove_directories_from_path(path_of_dir_to_look_for, dir_name_to_filter):
    matches = find_directories(path_of_dir_to_look_for, dir_name_to_filter)
    remove_directories(matches)


def remove_directories(matches):
    for match in matches:
        if os.path.isdir(match):
            try:
                shutil.rmtree(match)
            except:
                continue


def find_directories(path_of_dir_to_look_for, dir_name_to_filter):
    matches = []
    for root, directoryNames, filenames in os.walk(path_of_dir_to_look_for):
        for name in dir_name_to_filter:
            for dirname in fnmatch.filter(directoryNames, name):
                matches.append(os.path.join(root, dirname))
    return matches


if dir_exists(pathOfDirToLookFor):
    dirNameToFilter = ['Release', 'Debug', '.vs', '.vscode', 'out', 'cmake-build-debug-cygwin', 'cmake-build-debug-visual-studio', 'cmake-build-debug', 'cmake-build-release', 'build']
    remove_directories_from_path(pathOfDirToLookFor, dirNameToFilter)
