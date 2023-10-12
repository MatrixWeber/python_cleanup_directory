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
import subprocess
import tarfile
from tqdm import tqdm


def extract_tar_with_progress(tar_file_path, output_directory):
    with tarfile.open(tar_file_path, 'r:gz') as tar:
        members = tar.getmembers()
        total_files = len(members)

        for member in tqdm(members, desc="Extracting", unit="file"):
            tar.extract(member, output_directory)


pathOfDirToLookFor = '/home/z002wydr/Downloads/'


def parse_command_line():
    global args
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_dir', type=str, nargs='?', default=path_to_default_directory,
                        help="The main target directory e.g. '/home/z002wydr/target_directory/'")
    parser.add_argument('--source_dir', type=str, nargs='?', default=pathOfDirToLookFor,
                        help="The source directory to clean up e.g. '/home/z002wydr/Downloads'")
    parser.add_argument('-v', '--verbose', help='verbose mode including notifications', action='store_true')
    parser.add_argument('-x', "--extract", help='try to extract if possible', action='store_true')
    args = parser.parse_args()
    return args


args = parse_command_line()


verbose = args.verbose
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
tar_path = zip_path + 'tar/'
tmpPath = dest_dir + 'tmp/'
misc_path = dest_dir + 'misc/'
bin_path = dest_dir + 'bin/'
fpga_path = dest_dir + 'bin/fpga/'
elf_path = dest_dir + 'bin/elf/'
linux_deb_path = dest_dir + 'deb/'

old_file = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

file_extension_paths = {
    '.png': picture_path,
    '.jpg': picture_path,
    '.zip': zip_path,
    '.7z': zip_path,
    '.tar': tar_path,
    '.gz': tar_path,
    '.sof': fpga_path,
    '.sopcinfo': fpga_path,
    '.bin': bin_path,
    '.elf': elf_path,
    '.doc': doc_path,
    '.docx': doc_path,
    '.pdf': pdf_path,
    '.ppt': pptPath,
    '.pptx': pptPath,
    '.xml': xml_path,
    '.txt': txt_path,
    '.xls': excel_path,
    '.xlsx': excel_path,
    '.deb': linux_deb_path,
    '.rpm': linux_deb_path,
    '.odp': default_doc_path + 'linux/' + '.odp',
    '.ods': default_doc_path + 'linux/' + '.ods',
    '.odt': default_doc_path + 'linux/' + '.odt',
    '.odg': default_doc_path + 'linux/' + '.odg',
    '.mp4': video_path,
    '.mov': video_path,
}


def move_files_and_extract(source_file_path, dest_file_path):
    shutil.move(source_file_path, dest_file_path)
    if args.extract:
        if verbose:
            notify('Cleanup Script',
                   "Extracting file name " + dest_file_path + " ...\n")
            print("Extracting file name " + dest_file_path + " ...\n")
        extract_tar_with_progress(dest_file_path, tar_path)


def loop_over_all_file_in_given_dir(source_dir):
    global old_file
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
        dest = file_extension_paths.get(file_extension.lower(), misc_path)
        if not os.path.exists(dest):
            os.makedirs(dest)
        dest_file = dest + "/" + file_name_str
        if os.path.exists(dest_file):
            if verbose:
                notify('Cleanup Script', 'File: ' + dest_file + ' already exists on dest:' + dest)
            ask_question_and_perform_action(source_file, dest, file_name_str, verbose, move_files_and_extract)
        else:
            move_files_and_extract(source_file, dest_file)


while True:
    source_directory = args.source_dir
    if dir_exists(source_directory):
        loop_over_all_file_in_given_dir(source_directory)
    sleep(5)
