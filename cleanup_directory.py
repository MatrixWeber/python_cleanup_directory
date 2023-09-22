#!/usr/bin/python3

import os
import shutil
from time import sleep
from ask_question_and_perform_action import ask_question_and_perform_action
from write_msg_to_desktop import notify  # , speek
from verbose import checkIfVerbose
from check_if_dir_exists import dir_exists
import pathlib
from default_directory import path_to_default_directory
import argparse

pathOfDirToLookFor = '/home/z002wydr/Downloads'


def parse_command_line():
    global args
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_dir', type=str, nargs='?', default=pathOfDirToLookFor,
                        help="The source directory to clean up e.g. '/home/z002wydr/Downloads'")
    parser.add_argument('--target_dir', type=str, nargs='?', default=path_to_default_directory,
                        help="The main target directory e.g. '/home/z002wydr/target_directory/'")
    parser.add_argument('v', type=str, help='verbose mode including notifications', nargs='?', default=None)
    args = parser.parse_args()
    return args


args = parse_command_line()


verbose = args.v
source_dir = args.source_dir
dest_dir = args.target_dir

picture_path = dest_dir + 'pictures/'

video_path = dest_dir + 'videos/'
default_doc_path = dest_dir + 'doc/'
doc_path = default_doc_path + 'microsoft/doc/'
pdf_path = default_doc_path + 'pdf/'
pptPath = dest_dir + 'microsoft/ppt/'
xml_path = dest_dir + 'xml/'
txt_path = dest_dir + 'txt/'
excel_path = default_doc_path + 'microsoft/excel/'
zip_path = dest_dir + 'zip/'
tmpPath = dest_dir + 'tmp/'
misc_path = dest_dir + 'misc/'
bin_path = dest_dir + 'bin/'
fpga_path = dest_dir + 'bin/fpga/'
elf_path = dest_dir + 'bin/elf/'
linux_deb_path = dest_dir + 'deb/'

old_file = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

while True:
    if dir_exists(source_dir):
        for file in os.listdir(source_dir):
            file_name_str = str(file)
            file_extension = pathlib.Path(file_name_str).suffix.lower()
            if '.crdownload' in file_extension:
                if old_file not in file_name_str:
                    if verbose:
                        notify('Cleanup Script',
                               "New file is comming: " + file_name_str + "!\nFile will be moved to the given directory after downloading!\n")
                    old_file = file_name_str
                continue
            source_file = source_dir + '/' + file_name_str
            if '.png' in file_extension or '.jpg' in file_extension:
                dest = picture_path
            elif '.zip' in file_extension or '.7z' in file_extension or '.tar' in file_name_str.lower():
                dest = zip_path
            elif '.sof' in file_extension or '.sopcinfo' in file_extension:
                dest = fpga_path
            elif '.bin' in file_extension:
                dest = bin_path
            elif '.elf' in file_extension:
                dest = elf_path
            elif '.doc' in file_extension or '.docx' in file_extension:
                dest = doc_path
            elif '.pdf' in file_extension:
                dest = pdf_path
            elif '.ppt' in file_extension or '.pptx' in file_extension:
                dest = pptPath
            elif '.xml' in file_extension:
                dest = xml_path
            elif '.txt' in file_extension:
                dest = txt_path
            elif '.xls' in file_extension or '.xlsx' in file_extension:
                dest = excel_path
            elif '.deb' in file_extension or '.rpm' in file_extension:
                dest = linux_deb_path
            elif '.odp' in file_extension or '.ods' in file_extension or '.odt' in file_extension or '.odg' in file_extension:
                dest = default_doc_path + 'linux/' + file_extension
            elif '.mp4' in file_extension or '.mov' in file_extension:
                dest = video_path
            else:
                dest = misc_path
            if not os.path.exists(dest):
                os.makedirs(dest)
            dest_file = dest + "/" + file_name_str
            lambda_func = lambda source_file_path, dest_file_path: shutil.move(source_file_path, dest_file_path)
            if os.path.exists(dest_file):
                if verbose:
                    notify('Cleanup Script', 'File: ' + dest_file + ' already exists on dest:' + dest)
                ask_question_and_perform_action(source_file, dest, file_name_str, verbose, lambda_func)
            else:
                lambda_func(source_file, dest)
    sleep(10)
