'''
File Integrity Monitor 
Short script to determine if a file's trust overtime.
Jarrod Li
'''

import os
import time
import json
import hashlib
import logging
import datetime

DIR = "/Users/jarrod/cs6841/something-awesome/data/"

FIM_F = "s_files.json"

def analyse_dir():

    logging.basicConfig(filename='fimLog',
                            filemode='a',
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

    logging.info("File Integrity Monitoring")

    while True:
        read_dir()
        time.sleep(5)

def read_dir():

    os.chdir(DIR)
    directory = os.fsencode(DIR)

    s_arr = {}
    
    for file in os.listdir(directory):
        if os.path.isdir(file):
            continue

        
        file_name = os.fsencode(file).decode('UTF-8')
        cf = open(file_name, "rb")
        m = hashlib.md5()

        byte_stream = True
        while byte_stream:
            byte_stream = cf.read(1024)
            m.update(byte_stream)
            if file_name not in s_arr:
                s_arr[file_name] = []
            s_arr[file_name].append(m.hexdigest())
        
        cf.close()

    compare_hash(FIM_F, s_arr)
    with open(FIM_F, 'w') as jfile:
        json.dump(s_arr, jfile)
    


def compare_hash(file, ndct):

    os.chdir("../")
    
    logger = logging.getLogger('fim')

    cmp = {}
    with open(file, "r+") as file:
        cmp = json.load(file)

    for k,v in ndct.items():
        if k not in cmp:
            logger.info('new file detected: %s' % k)
        elif set(cmp[k]) != set(ndct[k]):
            logger.warning('file %s has changed!' % k)

if __name__ == "__main__":
    analyse_dir()