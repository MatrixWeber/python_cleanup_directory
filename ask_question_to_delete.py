import subprocess, os, platform
from write_msg_to_desktop import notify
from verbose import checkIfVerbose

def askQuestionAndPerform(destDirection, fileName, sayYesToString = '/][??05436'):
    destFile = destDirection + fileName
    if sayYesToString in fileName:
        deleteOptions = 'y'
    else:
        if checkIfVerbose():
            notify('Cleanup Script', 'Sure you wanna delete that file: ' + destFile + '?\nChoose option: y to delete, n to hold, o to open with a default program or r to rename file\n')
        deleteOptions = input("Sure you wanna delete that file: " + destFile + "?\nChoose option: y to delete, n to hold, o to open with a default program or r to rename file\n")
    if "yes" in deleteOptions or "y" in deleteOptions:
        os.remove(destFile)
        if checkIfVerbose():
            notify('Cleanup Script', destFile + ': was moved to trash\n')
    elif "o" in deleteOptions or "open" in deleteOptions:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', destFile))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(destFile)
        else:                                   # linux variants
            subprocess.call(('xdg-open', destFile))
        askQuestionAndPerform(destDirection, fileName)
    elif "r" in deleteOptions or "rename" in deleteOptions:
        if checkIfVerbose():
            notify('Cleanup Script', 'Enter new file name!\n')
        newFileName = input("Enter new file name!\n")
        os.rename(destFile, destDirection + newFileName)