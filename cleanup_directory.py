import os 
import shutil
from time import sleep
from ask_question_to_delete import  askQuestionAndPerform
from write_msg_to_desktop import notify, speek
from verbose import checkIfVerbose
from check_if_dir_exists import dir_exists
import pathlib

#pathOfDirToLookFor = input('Path to the directory to look for: ')
pathOfDirToLookFor = '/home/z002wydr/Downloads'

#picturePath = input('Path to the directory to store your pictures: ')
picturePath = '/home/z002wydr/Pictures/'

videoPath = input('Path to the directory to store your videos: ')

#docPath = input('Path to the directory to store your doc files: ')
docPath = '/home/z002wydr/Documents/new/microsoft/doc/'

#pptPath = input('Path to the directory to store your ppt files: ')
pptPath = '/home/z002wydr/Documents/new/microsoft/ppt/'

#xmlPath = input('Path to the directory to store your xml files: ')
xmlPath = '/home/z002wydr/xml/'

#txtPath = input('Path to the directory to store your txt files: ')
txtPath = '/home/z002wydr/Documents/new/txt/'

#excelPath = input('Path to the directory to store your excel files: ')
excelPath = '/home/z002wydr/Documents/new/microsoft/excel/'

#zipPath = input('Path to the directory to store your zip files: ')
zipPath = '/home/z002wydr/tmp/'

#fpgaPath = input('Path to the directory to store your fpga files: ')
fpgaPath = '/home/z002wydr/workspace/pluscontrol_master/bin/fpga/'

linuxDebPath = '/home/z002wydr/deb/'

oldFile = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

while True:
    if dir_exists(pathOfDirToLookFor):
        for file in os.listdir(pathOfDirToLookFor):
            fileNameStr = str(file)
            fileExtension = pathlib.Path(fileNameStr).suffix
            if '.crdownload' in fileExtension:
                if oldFile not in fileNameStr:
                    if checkIfVerbose():
                        speek("New file is comming: " + fileNameStr + "!\nFile will be moved to the given directory after downloading!\n")
                        notify('Cleanup Script', "New file is comming: " + fileNameStr + "!\nFile will be moved to the given directory after downloading!\n")
                    oldFile = fileNameStr
                continue
            pathToFileToMove = pathOfDirToLookFor + '/' + fileNameStr
            if '.png' in fileExtension or '.jpg' in fileExtension:
                dest = picturePath
            elif '.zip' in fileExtension or '.7z' in fileExtension or '.gz' in fileExtension or '.tar' in fileExtension:
                dest = zipPath
            elif '.sof' in fileExtension or '.sopcinfo' in fileExtension:
                dest = fpgaPath
            elif '.doc' in fileExtension or '.docx' in fileExtension:
                dest = docPath
            elif '.ppt' in fileExtension or '.pptx' in fileExtension:
                dest = pptPath            
            elif '.xml' in fileExtension:
                dest = xmlPath
            elif '.txt' in fileExtension:
                dest = txtPath
            elif '.xls' in fileExtension or '.xlsx' in fileExtension:
                dest = excelPath
            elif '.deb' in fileExtension or '.rpm' in fileExtension:
                dest = linuxDebPath
            else:
                continue
            if not os.path.exists(dest):
                os.makedirs(dest)
            destFile = dest + fileNameStr
            if os.path.exists(destFile):
                if checkIfVerbose():
                    notify('Cleanup Script', 'File: ' + destFile + ' already exists on dest:' + dest)
                askQuestionAndPerform(dest, fileNameStr)
            shutil.move(pathToFileToMove, dest)
            if checkIfVerbose():
                notify('Cleanup Script', 'File ' + fileNameStr + ' was moved to dir: ' + dest)
    sleep(10)