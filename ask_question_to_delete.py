import subprocess, os, platform
from write_msg_to_desktop import notify
from verbose import checkIfVerbose
import shutil
from default_directory import pathToDefaultDirectory

chooseString = '''Choose option: 'y' to remove (replace), 'n' to hold (but make a copy), 'o' open to inspect with a default program, 'r' to rename file (but keep the origin) or 'a' to remove (replace) all in a directory'''

def askQuestionAndPerform(destDirection, fileName, verbose, sayYesToString = '/][??05436'):
    destFile = destDirection + fileName
    if sayYesToString in fileName:
        deleteOptions = 'y'
    else:
        if verbose:
            notify('Cleanup Script', 'Sure you wanna replace that file: ' + destFile + ' ???\n' + chooseString + '\n')
            print('Cleanup Script', 'Sure you wanna replace that file: ' + destFile + ' ???\n' + chooseString + '\n')
        deleteOptions = input('Sure you wanna replace that file: ' + destFile + ' ???\n' + chooseString + '\n')
    if "yes" in deleteOptions or "y" in deleteOptions:
        if os.path.isdir(destFile):
            shutil.rmtree(destFile)
        else:
            os.remove(destFile)
        if verbose:
            notify('Cleanup Script', destFile + ': was moved to trash\n')
            print('Cleanup Script', destFile + ': was moved to trash\n')
    elif "o" in deleteOptions or "open" in deleteOptions:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', destFile))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(destFile)
        else:                                   # linux variants
            subprocess.call(('xdg-open', destFile))
        askQuestionAndPerform(destDirection, fileName, verbose)
    elif "r" in deleteOptions or "rename" in deleteOptions:
        if verbose:
            notify('Cleanup Script', 'Enter new file name!\n')
            print('Cleanup Script', 'Enter new file name!\n')
        newFileName = input("Enter new file name!\n")
        os.rename(destFile, destDirection + '/' + newFileName)
    elif "n" in deleteOptions or "no" in deleteOptions:
        if verbose:
            notify('Cleanup Script', 'Let this file untouched!\n')
            print('Cleanup Script', 'Let this file untouched!\n')
        os.rename(destFile, destFile + "_copy")
    elif "a" in deleteOptions:
        if verbose:
            notify('Cleanup Script', 'Remove all files from dir!\n')
            print('Cleanup Script', 'Remove all files from dir!\n')
        print('Directories and Files to remove: ')
        for file in os.listdir(pathToDefaultDirectory):
            fileNameStr = str(file)
            print('\t' + fileNameStr)
        deleteOptions = input('Sure you wanna remove all those files in given directory "' + pathToDefaultDirectory + '" ???\n y or n?\n')
        if "yes" in deleteOptions or "y" in deleteOptions:
            subprocess.call(('rm -rf', pathToDefaultDirectory + '*'))