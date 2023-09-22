import subprocess, os, platform
from write_msg_to_desktop import notify
from verbose import checkIfVerbose
import shutil
from default_directory import path_to_default_directory

chooseString = '''Choose option: 'y' to remove (replace), 'n' to hold (but make a copy), 'o' open to inspect with a default program, 'r' to rename file (but keep the origin) or 'a' to remove (replace) all in a directory'''


def ask_question_and_perform_action(source_file, dest_directory, file_name, verbose, lambda_func=None,
                                    say_yes_to_string='/][??05436'):
    dest_file = dest_directory + file_name
    if say_yes_to_string in file_name:
        delete_options = 'y'
    else:
        if verbose:
            notify('Cleanup Script', 'Sure you wanna replace that file: ' + dest_file + ' ???\n' + chooseString + '\n')
        delete_options = input('Sure you wanna replace that file: ' + dest_file + ' ???\n' + chooseString + '\n')
    if "yes" in delete_options or "y" in delete_options:
        if os.path.isdir(dest_file):
            shutil.rmtree(dest_file)
        else:
            os.remove(dest_file)
        if verbose:
            notify('Cleanup Script', dest_file + ': was moved to trash\n')
            print('Cleanup Script', dest_file + ': was moved to trash\n')
        if lambda_func:
            lambda_func(source_file, dest_file)
            if verbose:
                notify('Cleanup Script', 'File ' + source_file + ' was moved to dir: ' + dest_file)
    elif "o" in delete_options or "open" in delete_options:
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', dest_file))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(dest_file)
        else:  # linux variants
            subprocess.call(('xdg-open', dest_file))
        ask_question_and_perform_action(source_file, dest_directory, file_name, lambda_func, verbose)
    elif "r" in delete_options or "rename" in delete_options:
        if verbose:
            notify('Cleanup Script', 'Enter new file name!\n')
            print('Cleanup Script', 'Enter new file name!\n')
        new_file_name = input("Enter new file name!\n")
        if lambda_func:
            if verbose:
                notify('Cleanup Script', 'Renamed file to ' + new_file_name + '!\n')
                print('Cleanup Script', 'Renamed file to ' + new_file_name + '!\n')
            lambda_func(source_file, dest_directory + '/' + new_file_name)
            if verbose:
                notify('Cleanup Script', 'File ' + source_file + ' was moved to dir: ' + dest_directory + '/' + new_file_name)
    elif "n" in delete_options or "no" in delete_options:
        if verbose:
            notify('Cleanup Script', 'Let this file untouched (but make a copy)!\n')
            print('Cleanup Script', 'Let this file untouched (but make a copy)!\n')
        if lambda_func:
            lambda_func(source_file, dest_file + "_copy")
            if verbose:
                notify('Cleanup Script', 'File ' + source_file + ' was moved to dir: ' + dest_file + "_copy")
    elif "a" in delete_options:
        say_yes_to_string = dest_file
        ask_question_and_perform_action(source_file, dest_directory, file_name, verbose, lambda_func, say_yes_to_string)
