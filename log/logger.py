# Author: harry.cai
# DATE: 2018/2/1

import logging
import os
from config import setting


def log_func(log_type):
    ''' 创建日志对象 '''

    logger = logging.getLogger(setting.LogType[log_type])
    logger.setLevel(setting.LogLevel['global'])

    log_file_path = os.path.join(setting.LOGGER_DB_PATH, '%s.txt' % setting.LogType[log_type] )
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(setting.LogLevel['file'])
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(setting.LogLevel['console'])
    logger.addHandler(sh)

    fh_format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    sh_format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    sh.setFormatter(sh_format)
    fh.setFormatter(fh_format)

    return logger

