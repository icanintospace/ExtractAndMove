# This script is meant for passing in a folder as an argument, and extracting all rar files within those folders
# subfolders. Afterwards, we move the extracted files to a predetermined location.

import os
import subprocess
import argparse

# TODO: Change default output to a configuration file
default_output = '/home/deschain/PlexLibrary'

parser = argparse.ArgumentParser(description='Extract .rar files in the given folder and its subfolders, and move them '
                                             'to the specified destination.')
parser.add_argument('s', metavar='source', help='The source folder for archives to extract')
parser.add_argument('-o', metavar='output', help='Output folder for extracted archives', default=default_output)
args = parser.parse_args()

if os.path.isdir(args.s):
    working_path = os.path.abspath(args.s)
else:
    print("Please enter a valid path")
output_path = os.path.normpath(args.o)

# Going through every subfolder and file in working_path
for folderName, subfolders, filenames in os.walk(working_path):
    # current working directory
    print('Current folder: ' + folderName)

    # current subfolder
    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)

    # current file
    for filename in filenames:
        # if .rar file found, extract using p7zip
        if filename.endswith('.rar'):
            print('Archive inside ' + folderName + ': ' + filename)

            # First we create a list of existing files for reference
            files_pre = []
            for file in os.listdir(folderName):
                if os.path.isfile(os.path.join(folderName, file)):
                    files_pre.append(file)
            print(files_pre)
            # We combine variable to get the full path
            full_path = folderName + '/' + filename

            # Then we extract the .rar file found
            subprocess.call(["7z", "x", full_path])

            # We now create a new list of files for reference to determine the names of the new files
            files_post = []
            for file in os.listdir(folderName):
                if os.path.isfile(os.path.join(folderName, file)):
                    files_post.append(file)

            # Next is determining which files are new
            files_new = list(list(set(files_pre)-set(files_post)) + list(set(files_post)-set(files_pre)))

            # We move the extracted file into the predetermined directory
            output_folder = "/home/berk/testing/"
            for i in files_new:
                new_file = folderName + '/' + i
                subprocess.call(["mv", new_file, output_folder])

    print('')
