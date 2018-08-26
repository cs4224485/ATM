# Author: harry.cai
# DATE: 2018/2/1
import json
import os
from shopping.user_db import account
from shopping.setting import config


def auth (username, password):
    ''' 用户验证 '''
    filename = os.path.join(config.USER_DB_PATH, username)
    if os.path.isfile(filename):
        user_data = json.load(open(filename, 'r'))
        if username == user_data['username'] and password == user_data ['password']:
            return user_data


def login (user_info):
    ''' 用户登录 '''
    count = 0
    while count < 3:
        inp_username = input('请输入用户名：')
        inp_password = input('请输入密码：')
        user_data = auth(inp_username, inp_password)
        if user_data:
            user_info['is_authentication'] = True
            user_info['user_data'] = user_data
            return user_info
        else:
            print('用户名或密码错误！')
        count+=1