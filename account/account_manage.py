# Author: harry.cai
# DATE: 2018/1/31
import json
import pickle
import os
from config import setting


def account_save(user_data, kind):
    '''
    存储用户信息
    :param user_data: 用户数据
    :param kind: 用户类型，管理员或普通用户
    :return:
    '''
    if kind == 'common_user':
        path = setting.USER_DB_PATH
        file_name = os.path.join(path, user_data['id'])
        json.dump(user_data, open('%s.json' % file_name, 'w', encoding='utf8'))
        return True
    elif kind == 'admin':
        path = setting.ADMIN_DB_PATH
        file_name = os.path.join(path, user_data.username)
        pickle.dump(user_data, open(file_name, 'wb'))
        return True


def account_load(username, kind):
    """
    加载数据
    :param username:
    :param kind: 用户类型，管理员或普通用户
    :return:
    """
    if kind == 'common_user':
        path = setting.USER_DB_PATH
        file_name = os.path.join(path, username)
        if os.path.exists('%s.json' % file_name):
            data = json.load(open('%s.json' % file_name, 'r', encoding='utf8'))
            return data
    elif kind == 'admin':
        path = setting.ADMIN_DB_PATH
        file_name = os.path.join(path, username)
        if os.path.exists(file_name):
            data = pickle.load(open(file_name, 'rb'))
            return data
