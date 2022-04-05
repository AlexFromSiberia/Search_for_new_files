import os
import time
from datetime import datetime

TIME_BORDER = 86400
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'
CHECK_DIR = r'D:\Python\Python_life_hacks'
FILE_LOG = r'D:\Python\Python_life_hacks\Search_for_new_files\log.txt'


def clear_log():
    # open & close - it's enough to clear all data
    f = open(FILE_LOG, 'w')
    f.close()


def find_virus(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            file = os.path.join(root, name)
            if check(file):
                add_to_log(file)


def check(file):
    current_ts = time.time()
    change_time = get_change_time(file)
    return current_ts - change_time < TIME_BORDER


def get_change_time(file):
    modification_time = os.stat(file).st_mtime
    atrib_change_time = os.stat(file).st_atime
    creation_time  =    os.stat(file).st_ctime
    return max(modification_time, atrib_change_time, creation_time)


def add_to_log(file):
    add_string = file + ':' + datetime.fromtimestamp(get_change_time(file)).strftime(DATE_FORMAT) + "\n"
    f = open(FILE_LOG, 'a')
    f.write(add_string)
    f.close()


if __name__ == '__main__':
    clear_log()
    find_virus(CHECK_DIR)












