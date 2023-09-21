import os

def dir_exists(directory):
    if os.path.exists(directory):
        return True
    else:
        print(directory + ': directory does not exists')
        return False