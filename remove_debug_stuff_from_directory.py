#!/usr/bin/python3

import os
import shutil
import fnmatch
from check_if_dir_exists import dir_exists
import argparse

path_of_dir_to_look_for = r'C:\Users\SW\Desktop\MicroConsult\Clean Code\OOPFCPP'
dir_names_to_filter = ['Release', 'Debug', '.vs', '.vscode', 'out', 'cmake-build-debug-cygwin', 'cmake-build-debug-visual-studio', 'cmake-build-debug', 'cmake-build-release', 'build', '.idea', 'x64']


def remove_directories_from_path(path_of_dir, dir_name_to_filter):
    matches = find_directories(path_of_dir, dir_name_to_filter)
    remove_directories(matches)


def remove_directories(matches):
    for match in matches:
        if os.path.isdir(match):
            try:
                shutil.rmtree(match)
            except:
                continue


def find_directories(path_of_dir, dir_name_to_filter):
    matches = []
    for root, directoryNames, filenames in os.walk(path_of_dir):
        for name in dir_name_to_filter:
            for dirname in fnmatch.filter(directoryNames, name):
                matches.append(os.path.join(root, dirname))
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str, default=path_of_dir_to_look_for, help='The directory to recursively delete from', nargs='?')
    parser.add_argument('dir_names', type=str, default=dir_names_to_filter, help='Directories to search for removing', nargs='*')
    args = parser.parse_args()

    if dir_exists(args.directory):
        remove_directories_from_path(args.directory, args.dir_names)
