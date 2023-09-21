import os
import shutil
from ProgressBar import ProgressBar

 
def countFiles(directory):
    files = []
 
    if os.path.isdir(directory):
        for path, dirs, filenames in os.walk(directory):
            files.extend(filenames)
 
    return len(files)

def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

 
def moveFilesWithProgress(src, dest):
    p = ProgressBar('Copying files...')
    numFiles = countFiles(src)
 
    if numFiles > 0:
        makedirs(dest)
 
        numCopied = 0
 
        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                destDir = path.replace(src,dest)
                makedirs(os.path.join(destDir, directory))
            
            for sfile in filenames:
                srcFile = os.path.join(path, sfile)
 
                destFile = os.path.join(path.replace(src, dest), sfile)
                
                shutil.move(srcFile, destFile)
                
                numCopied += 1
                
                p.calculateAndUpdate(numCopied, numFiles)

def copyFilesWithProgress(src, dest):
    p = ProgressBar('Copying files...')
    numFiles = countFiles(src)
 
    if numFiles > 0:
        makedirs(dest)
 
        numCopied = 0
 
        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                destDir = path.replace(src,dest)
                makedirs(os.path.join(destDir, directory))
            
            for sfile in filenames:
                srcFile = os.path.join(path, sfile)
 
                destFile = os.path.join(path.replace(src, dest), sfile)
                
                shutil.copy(srcFile, destFile)
                
                numCopied += 1
                
                p.calculateAndUpdate(numCopied, numFiles)

copyFilesWithProgress('/home/z002wydr/bla/', '/home/z002wydr/tmp/' )