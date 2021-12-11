# This script updates the tf-es-dumping TaoSJ Data Directory with the new TaoSJ Data Directory from
# TaoSJDL. Before doing this, the tf-es-dumping TaoSJ Data Directory will be copied to the TaoSJDL backup
# directory to serve as backup in case any corruption of files happens

import glob
import pytoml
from datetime import date
import os
import shutil
from pathlib import Path

CONFIG_PATH = 'config.toml'


def read_config(path):
    config = pytoml.load(open(path, 'rb'))
    return config


if __name__ == '__main__':

    # Move to TaoSJDL TaoSJ Data Directory
    config_file = read_config(CONFIG_PATH)
    copy_cwd = str(Path(os.getcwd()).parent)
    os.chdir(os.getcwd() + config_file['tf-es-dumping_integration']['TaoSJDL_TaoSJ_Data'])

    all_files = glob.glob("**/*", recursive=True)

    # Move to tf-es-dumping TaoSJ Data
    os.chdir("..\\..\\.." + config_file['tf-es-dumping_integration']['tf-es-dumping_TaoSJ_Data'])
    backup_dest_path = copy_cwd + config_file['tf-es-dumping_integration']['TaoSJ_Data_backup']
    #copy = shutil.copytree(os.getcwd(), backup_dest_path + "\\ Backup " + date.today().strftime('%Y-%m-%d'))

# TODO: Scan TaoSJDL TaoSJ Data Directory to check that all files are in .xlsx format


# TODO: If above condition fulfilled, then go to tf-es-dumping TaoSJ Data and move the entire folder to
# TODO: tf-es-dumping (TaoSJ Data backup), creating a subfolder with the date in the process

# TODo: Copy the TaoSJ Data from TAOSJDL over to tf-es-dumping TaoSJ Data, thereafter process is finished
