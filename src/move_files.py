import glob
import os
import shutil


def read_directory(folder_path):
    search = folder_path + '\\*.xls'
    list_files = glob.glob(search, recursive=True)
    return list_files


def read_directory_xlsx(folder_path):
    search = folder_path + '\\*.xlsx'
    list_files = glob.glob(search, recursive=True)
    return list_files


def rename_files(list_files):
    for files in list_files:
        pre, ext = os.path.splitext(files)
        os.rename(files, pre + '.xlsx')


def shift_files(download_sku, old_file_path, list_of_dicts):
    for dicts in list_of_dicts:
        if dicts['sku_id'] == download_sku:
            try:
                file_dest = dicts['dest_path']
                print(f"Shifting {download_sku} from {old_file_path} to {file_dest}...")
                shutil.copy(old_file_path, file_dest)
                print("Successfully copied.")
            except KeyError:
                print(dicts['sku_id'])
                print(download_sku)
                pass


