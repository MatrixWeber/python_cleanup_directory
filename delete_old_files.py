from time import strftime, localtime
import os
from ask_question_to_delete import  askQuestionAndPerform
from check_if_dir_exists import dir_exists


#dirPath = input('Path to the directory to delete your files: ')
dirPath = '/home/z002wydr/Documents/new/'

yearAndDateStr = '2020-10-23-15-30-00'
monthAndYearList = yearAndDateStr.split('-')
monthAndYear = monthAndYearList[0] + monthAndYearList[1]+ monthAndYearList[2]+ monthAndYearList[3]+ monthAndYearList[4]+ monthAndYearList[5]

if dir_exists(dirPath):
    for file in os.listdir(dirPath):
        fileNameStr = str(file)
        destFile = dirPath + fileNameStr
        if os.path.isdir(destFile):
            for file in os.listdir(destFile):
                modTimesinceEpoc = os.path.getmtime(destFile + "/" + file)
                modificationTime = strftime('%Y-%m-%d %H:%M:%S', localtime(modTimesinceEpoc))
                monthAndYearOfFileList = modificationTime.split('-')
                monthAndYearOfFile = monthAndYearOfFileList[0] + monthAndYearOfFileList[1] + monthAndYearOfFileList[2]
                monthAndYearOfFile = monthAndYearOfFile.split(" ")
                splitTime = monthAndYearOfFile[1].split(":")
                dayMonthYearAndTimeOfFile = monthAndYearOfFile[0] + splitTime[0] + splitTime[1] + splitTime[2]
                if dayMonthYearAndTimeOfFile < monthAndYear:
                    print("Last Modified Time : ", modificationTime )
                    askQuestionAndPerform(destFile + "/", file, 'Bildschirmfoto')
        modTimesinceEpoc = os.path.getmtime(destFile)
        modificationTime = strftime('%Y-%m-%d %H:%M:%S', localtime(modTimesinceEpoc))
        monthAndYearOfFileList = modificationTime.split('-')
        monthAndYearOfFile = monthAndYearOfFileList[0] + monthAndYearOfFileList[1] + monthAndYearOfFileList[2]
        if monthAndYearOfFile < monthAndYear:
            print("Last Modified Time : ", modificationTime )
            askQuestionAndPerform(dirPath, fileNameStr, 'Bildschirmfoto')