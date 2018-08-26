# Author: harry.cai
# DATE: 2018/1/31
from core import admin
from account import account_manage


def create_admin(username, password):
    '''
    创建管理员账号
    :param username:管理员账号
    :param password: 管理员密码
    :return:
    '''
    admin_obj = admin.admin_action(username, password)
    account_manage.account_save(admin_obj, 'admin')
    return True


def init():
    """
    初始化管理员账号
    :return:
    """
    inp_username = input('请设置用户名：')
    inp_password = input('请设置密码： ')
    is_saved = create_admin(inp_username, inp_password)
    if is_saved:
        print('初始化成功')