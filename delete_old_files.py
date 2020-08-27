from time import strftime, localtime
import os
from ask_question_to_delete import  askQuestionAndPerform
from check_if_dir_exists import dir_exists


dirPath = input('Path to the directory to delete your files: ')
dirPath = '/home/z002wydr/Downloads/'

yearAndDateStr = '2020-06'
monthAndYearList = yearAndDateStr.split('-')
monthAndYear = monthAndYearList[0] + monthAndYearList[1]

if dir_exists(dirPath):
    for file in os.listdir(dirPath):
        fileNameStr = str(file)
        destFile = dirPath + fileNameStr
        modTimesinceEpoc = os.path.getmtime(destFile)
        modificationTime = strftime('%Y-%m-%d %H:%M:%S', localtime(modTimesinceEpoc))
        monthAndYearOfFileList = modificationTime.split('-')
        monthAndYearOfFile = monthAndYearOfFileList[0] + monthAndYearOfFileList[1]
        if monthAndYearOfFile < monthAndYear:
            print("Last Modified Time : ", modificationTime )
            askQuestionAndPerform(dirPath, fileNameStr, 'Bildschirmfoto')