#!/usr/bin/python3

import os 
import shutil
from time import sleep
from ask_question_to_delete import  askQuestionAndPerform
from write_msg_to_desktop import notify #, speek
from verbose import checkIfVerbose
from check_if_dir_exists import dir_exists
import pathlib
from default_directory import pathToDefaultDirectory
import argparse


pathOfDirToLookFor = '/home/z002wydr/Downloads'


def parse_command_line():
    global args
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_dir', type=str, nargs='?', default=pathOfDirToLookFor,
                        help="The source directory to clean up e.g. '/home/z002wydr/Downloads'")
    parser.add_argument('--target_dir', type=str, nargs='?', default=pathToDefaultDirectory,
                        help="The main target directory e.g. '/home/z002wydr/target_directory/'")
    parser.add_argument('v', type=str, help='verbose mode including notifications', nargs='?', default=None)
    args = parser.parse_args()
    return args


args = parse_command_line()

picturePath = args.target_dir + '/pictures/'

videoPath = args.target_dir + '/videos/'
defaultDocPath = args.target_dir + '/doc/'
docPath = defaultDocPath + 'microsoft/doc/'
pdfPath = defaultDocPath + 'pdf/'
pptPath = args.target_dir + '/microsoft/ppt/'
xmlPath = args.target_dir + '/xml/'
txtPath = args.target_dir + '/txt/'
excelPath = defaultDocPath + 'microsoft/excel/'
zipPath = args.target_dir + '/zip/'
tmpPath = args.target_dir + '/tmp/'
miscPath = args.target_dir + '/misc/'
binPath = args.target_dir + '/bin/'
fpgaPath = args.target_dir + '/bin/fpga/'
elfPath = args.target_dir + '/bin/elf/'
linuxDebPath = args.target_dir + '/deb/'

oldFile = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

verbose = args.v

while True:
    if dir_exists(args.source_dir):
        for file in os.listdir(args.source_dir):
            fileNameStr = str(file)
            fileExtension = pathlib.Path(fileNameStr).suffix.lower()
            if '.crdownload' in fileExtension:
                if oldFile not in fileNameStr:
                    if verbose:
                        notify('Cleanup Script', "New file is comming: " + fileNameStr + "!\nFile will be moved to the given directory after downloading!\n")
                    oldFile = fileNameStr
                continue
            pathToFileToMove = args.source_dir + '/' + fileNameStr
            if '.png' in fileExtension or '.jpg' in fileExtension:
                dest = picturePath
            elif '.zip' in fileExtension or '.7z' in fileExtension or '.gz' in fileExtension or '.tar' in fileNameStr.lower():
                dest = zipPath
            elif '.sof' in fileExtension or '.sopcinfo' in fileExtension:
                dest = fpgaPath
            elif '.bin' in fileExtension:
                dest = binPath
            elif '.elf' in fileExtension:
                dest = elfPath
            elif '.doc' in fileExtension or '.docx' in fileExtension:
                dest = docPath
            elif '.pdf' in fileExtension:
                dest = pdfPath
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
            elif '.odp' in fileExtension or '.ods' in fileExtension or '.odt' in fileExtension or '.odg' in fileExtension:
                dest = defaultDocPath + 'linux/' + fileExtension
            elif '.mp4' in fileExtension or '.mov' in fileExtension:
                dest = videoPath
            else:
                dest = miscPath
            if not os.path.exists(dest):
                os.makedirs(dest)
            destFile = dest + "/" + fileNameStr
            if os.path.exists(destFile):
                if verbose:
                    notify('Cleanup Script', 'File: ' + destFile + ' already exists on dest:' + dest)
                askQuestionAndPerform(dest, fileNameStr, verbose)
            shutil.move(pathToFileToMove, destFile)
            if verbose:
                notify('Cleanup Script', 'File ' + fileNameStr + ' was moved to dir: ' + dest)
    sleep(10)