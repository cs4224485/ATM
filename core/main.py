# Author: harry.cai
# DATE: 2018/1/31
from account import account_manage
from core import authentication
from core import transaction
from log  import logger
import hashlib

# 用户状态信息
user_state = {
    'user_data': '',
    'is_login': False
}

# 日志对象
access_log = logger.log_func('access')
transaction_log = logger.log_func('transaction')


def transfer(user_data, transaction_log):
    """ 转账功能 """
    print('当前信用额度：%s\n'
          '当前可用余额：%s' % (user_data['credit_limit'], user_data['balance']))
    target_id = input('请输入目标用户ID：')
    amount = input('请输入转入金额：')
    if user_data['balance'] > int(amount):
        target_account = account_manage.account_load(target_id,'common_user')
        if target_account:
            state = transaction.transaction(user_data, 'transfer', amount, transaction_log, target_account)
            if state:
                print('转账成功, 当前可用余额:%s ' % user_data['balance'])
        else:
            print('用户不存在')
    else:
        print('账户余额不足')


def repay(user_data, transaction_log):
    ''' 还款功能 '''
    print('当前额度：%s\n'
          '当前余额：%s' % (user_data['credit_limit'], user_data['balance']))
    amount = input('请输入还款金额：')
    trans_state = transaction.transaction(user_data, 'repay', amount, transaction_log)
    if trans_state:
        print('还款成功, 当前可用余额:%s ' % user_data['balance'])


def withdraw(user_data, transaction_log):
    ''' 提现功能 '''
    print('当前额度：%s\n'
          '当前余额：%s' % (user_data['credit_limit'], user_data['balance']))
    amount = input('请提现金额：')
    if (user_data['balance'] / 2) > int(amount):
        trans_state = transaction.transaction(user_data, 'withdraw', amount, transaction_log)
        if trans_state:
            print('\033[32m取现成功，当前余额:%s \033[0m' % user_data['balance'])
    else:
        print('余额不足')


def show_info(user_data, *args):
    ''' 显示账户信息 '''
    print(' information '.center(40, '-'))
    for i in user_data:
        if i != 'password' and i != 'history_list':
            print('\033[32m%15s: %s\033[0m' % (i, user_data[i]))


def show_history(user_data, *args):
    ''' 查看历史账单 '''
    print(' history list '.center(40, '-'))
    for i in user_data['history_list']:
        print('\033[32m%s\033[0m' %i )


def modify_password(user_data, *args):
    ''' 修改密码 '''
    before_password = input('请输入原密码：')
    before_passwd_hash = hashlib.md5()
    before_passwd_hash.update(before_password.encode('utf8'))
    if before_passwd_hash.hexdigest() == user_data['password']:
        change_password = input('请输入新密码： ')
        change_passwd_hash = hashlib.md5()
        change_passwd_hash.update(change_password.encode('utf8'))
        user_data['password'] = change_passwd_hash.hexdigest()
        account_manage.account_save(user_data, 'common_user')
        print('\033[32m密码修改成功\033[0m')
    else:
        print('密码错误！')


def consume(consume_amount):
    ''' 用户消费 '''
    auth_data = consume_interface(user_state, access_log)
    if auth_data:
        if auth_data['user_data']['balance'] > int(consume_amount):
            trans_state = transaction.transaction(auth_data['user_data'], 'consume', consume_amount, transaction_log)
            if trans_state:
                print('\033[32m支付成功，当前余额：%s\033[0m'% auth_data['user_data']['balance'])
                auth_data['is_login'] = False
                return True
        else:
            auth_data['is_login'] = False
            print('\033[31m账号余额不足。\033[0m')
            return False


@authentication.login
def welcome():
    ''' 登录欢迎接口 '''
    print('Welcome to login')


@authentication.login
def consume_interface():
    ''' 消费登录接口 '''
    print('欢迎登录ATM系统')


def interactive(user_data, transaction_log):
    menu = '''\033[33m
    ------- ATM --------
        1  转账
        2  还款
        3  提现
        4  查看账户信息
        5  查看历史账单
        6  修改密码\033[0m
    '''
    dic_menu ={
        '1': transfer,
        '2': repay,
        '3': withdraw,
        '4': show_info,
        '5': show_history,
        '6': modify_password
    }
    while True:
        print(menu)
        choice = input('请选择[q退出]>>>')
        if choice in dic_menu:
            dic_menu[choice](user_data, transaction_log)
        if choice == 'q':
            break


def run():
    user_state_auth = welcome(user_state, access_log)
    if user_state_auth:
        interactive(user_state_auth['user_data'], transaction_log)

