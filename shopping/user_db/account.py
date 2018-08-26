# Author: harry.cai
# DATE: 2018/2/1
import json
import os
from shopping.setting import config


def save_info(user_data):
    ''' 保存账号信息 '''
    file_name = os.path.join(config.USER_DB_PATH, user_data['username'])
    json.dump(user_data, open(file_name, 'w'))
    return True