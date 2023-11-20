#!/usr/bin/python3

from time import strftime, localtime
import os
from ask_question_and_perform_action import ask_question_and_perform_action
from check_if_dir_exists import dir_exists
from default_directory import path_to_default_target_directory
import argparse


def parse_command_line():
    global args
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--cleanup_dir', type=str, nargs='?', default=path_to_default_target_directory,
                        help="The main cleanup directory e.g. '/home/z002wydr/cleanup_directory/'")
    parser.add_argument('-d', '--date', type=str, help="The date to perform cleanup from format should be like this 2023-09-01-15-30-00")
    parser.add_argument('-v', '--verbose', help='verbose mode including notifications', action='store_true')
    parser.add_argument('-y', "--yes", help='say yes for everything', action='store_true')
    args = parser.parse_args()
    return args


args = parse_command_line()

dirPath = args.cleanup_dir

yearAndDateStr = args.date
yearAndDateStrSplitted = yearAndDateStr.split('-')
if len(yearAndDateStrSplitted) != 6:
    print("Date format should be like this 2023-09-01-15-30-00")
    exit(1)

yearAndDateStr = '2023-09-01-15-30-00'
monthAndYearList = yearAndDateStr.split('-')
monthAndYear = monthAndYearList[0] + monthAndYearList[1] + monthAndYearList[2] + monthAndYearList[3] + monthAndYearList[
    4] + monthAndYearList[5]

if dir_exists(dirPath):
    for file in os.listdir(dirPath):
        fileNameStr = str(file)
        destFile = dirPath + fileNameStr
        if os.path.isdir(destFile):
            for file_dest in os.listdir(destFile):
                modTimesinceEpoc = os.path.getmtime(destFile + "/" + file_dest)
                modificationTime = strftime('%Y-%m-%d %H:%M:%S', localtime(modTimesinceEpoc))
                monthAndYearOfFileList = modificationTime.split('-')
                monthAndYearOfFile = monthAndYearOfFileList[0] + monthAndYearOfFileList[1] + monthAndYearOfFileList[2]
                monthAndYearOfFile = monthAndYearOfFile.split(" ")
                splitTime = monthAndYearOfFile[1].split(":")
                dayMonthYearAndTimeOfFile = monthAndYearOfFile[0] + splitTime[0] + splitTime[1] + splitTime[2]
                if dayMonthYearAndTimeOfFile < monthAndYear:
                    print("Last Modified Time : ", modificationTime)
                    ask_question_and_perform_action(None, destFile + "/", file_dest, args.verbose, yes=args.yes)
        modTimesinceEpoc = os.path.getmtime(destFile)
        modificationTime = strftime('%Y-%m-%d %H:%M:%S', localtime(modTimesinceEpoc))
        monthAndYearOfFileList = modificationTime.split('-')
        monthAndYearOfFile = monthAndYearOfFileList[0] + monthAndYearOfFileList[1] + monthAndYearOfFileList[2]
        if monthAndYearOfFile < monthAndYear:
            print("Last Modified Time : ", modificationTime)
            ask_question_and_perform_action(None, dirPath, fileNameStr, args.verbose,  yes=args.yes)
