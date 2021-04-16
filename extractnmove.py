# This script is meant for passing in a folder as an argument, and extracting all rar files within those folders
# subfolders. Afterwards, we delete the archive files while retaining the extracted file(s).

import os
import subprocess

# TODO: get the desired directory path from argument
working_path = '/mnt/data/Downloads/Ash.vs.Evil.Dead.S01E01.720p.BluRay.x264-DEMAND/'

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
            print('File inside ' + folderName + ': ' + filename)
            full_path = folderName + filename
            subprocess.call(["7z", "x", "-o" + folderName, full_path])

            # now remove


    print('')
