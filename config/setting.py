# Author: harry.cai
# DATE: 2018/1/31
import os
import logging
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_DB_PATH = os.path.join(BASEDIR, 'account', 'userdb')
ADMIN_DB_PATH = os.path.join(BASEDIR, 'account', 'admindb')
LOGGER_DB_PATH = os.path.join(BASEDIR, 'log', 'logdb')

# 日志类型
LogType = {
    'access': 'access_log',
    'transaction': 'transaction_log'
}


# 日志级别
LogLevel = {
    'global': logging.DEBUG,
    'console': logging.WARNING,
    'file': logging.INFO
}


# 交易类型
TransAction = {
    'transfer': {'method': 'plus_reduce', 'interest': 0},
    'repay': {'method': 'plus', 'interest': 0},
    'withdraw': {'method': 'reduce', 'interest': 0.05},
    'consume': {'method': 'reduce', 'interest': 0}
                            }


