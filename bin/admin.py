# Author: harry.cai
# DATE: 2018/1/31
''' 管理员登录接口 '''

import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

if __name__ == '__main__':
    from core import admin
    admin.admin_interface()