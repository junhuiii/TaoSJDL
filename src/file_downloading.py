import os
import time
import glob

class FileWaiter:

    def __init__(self, path):
        self.path = path
        self.files = set(glob.glob(path))

    def wait_new_file(self, timeout):
        """
        Waits for a new file to be created and returns the new file path.
        """
        endtime = time.time() + timeout
        while True:
            diff_files = set(glob.glob(self.path)) - self.files
            if diff_files :
                new_file = diff_files.pop()
                try:
                    os.rename(new_file, new_file)
                    self.files = set(glob.glob(self.path))
                    msg = f'{new_file} has been downloaded'
                    return msg
                except :
                    pass
            if time.time() > endtime:
                message = 'File did not download.'
                return message
            time.sleep(0.1)