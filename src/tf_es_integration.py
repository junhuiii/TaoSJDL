# This script updates the tf-es-dumping TaoSJ Data Directory with the new TaoSJ Data Directory from
# TaoSJDL. Before doing this, the tf-es-dumping TaoSJ Data Directory will be copied to the TaoSJDL backup
# directory to serve as backup in case any corruption of files happens

import glob
import pytoml
from datetime import date
import os
import shutil
import stat
import errno
from pathlib import Path

CONFIG_PATH = 'config.toml'


def read_config(path):
    config = pytoml.load(open(path, 'rb'))
    return config


def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(path)
    else:
        raise


if __name__ == '__main__':

    # Move to TaoSJDL TaoSJ Data Directory
    config_file = read_config(CONFIG_PATH)
    copy_cwd = str(Path(os.getcwd()).parent)
    os.chdir(os.getcwd() + config_file['tf-es-dumping_integration']['TaoSJDL_TaoSJ_Data'])

    # Copy files from tf-es-dumping TaoSJ Data to tf-es-dumping (TaoSJ Data backup)
    os.chdir("..\\..\\.." + config_file['tf-es-dumping_integration']['tf-es-dumping_TaoSJ_Data'])
    backup_dest_path = copy_cwd + config_file['tf-es-dumping_integration']['TaoSJ_Data_backup']
    copy = shutil.copytree(os.getcwd(), backup_dest_path + "\\ Backup " + date.today().strftime('%Y-%m-%d'))
    print("Folder created. Successfully created backup.")

    # Delete files in tf-es-dumping TaoSJ Data
    for direct in os.listdir(os.getcwd()):
        print(f'Deleting {direct} from tf-es-dumping...')
        shutil.rmtree(os.getcwd() + f'\\{direct}', ignore_errors=False, onerror=handleRemoveReadonly)
        print("Completed.")
    print("All folders deleted within tf-es-dumping, proceeding to copy updated data...")

    # Copy files from TaoSJDL TaoSJData to tf-es-dumping TaoSJ Data
    for directory in os.listdir(copy_cwd + "\\src" + config_file['tf-es-dumping_integration']['TaoSJDL_TaoSJ_Data']):
        print("Copying...")
        print(copy_cwd + "\\src" + config_file['tf-es-dumping_integration']['TaoSJDL_TaoSJ_Data'] + f"\\{directory}")
        shutil.copytree(copy_cwd + "\\src" + config_file['tf-es-dumping_integration']['TaoSJDL_TaoSJ_Data'] + f"\\{directory}", os.getcwd() + f"\\{directory}")
        print("Completed.")

    print("All folders copied over from TaoSJDL TaoSJData to tf-es-dumping TaoSJ Data. Entire process completed successfully.")