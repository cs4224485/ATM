# Author: harry.cai
# DATE: 2018/1/31
from config import setting
from account import account_manage
import time


def transaction(user_info, action, amount, transaction_log, target=None):
    '''
    处理账户交易模块
    :param user_info: 用户相关数据信息
    :param action: 所需进行的操作
    :param amount: 处理数额
    :param transaction_log: 交易记录日志
    :param target: 如果是转账的话需要目标账户
    :return:
    '''

    if action in setting.TransAction:
        if amount.isdigit():
            amount = float(amount)
            # 加载最新的余额数据
            new_balance = account_manage.account_load(user_info['id'], 'common_user')['balance']
            # 计算利息
            interest = amount * setting.TransAction[action]['interest']
            time_log = time.strftime('%Y-%m-%d %H:%M:%S')
            # 转账对用户进行加减操作
            if setting.TransAction[action]['method'] == 'plus_reduce':
                new_balance = new_balance - amount - interest
                user_info['balance'] = new_balance
                target['balance'] += amount
                # 存储目标账户信息
                account_manage.account_save(target, 'common_user')
            # 账户余额加减操作
            elif setting.TransAction[action]['method'] == 'plus':
                new_balance = new_balance + amount - interest
                user_info['balance'] = new_balance
            elif setting.TransAction[action]['method'] == 'reduce':
                new_balance = new_balance - amount - interest
                user_info['balance'] = new_balance

            user_info['history_list'].append('%s action:%s amount:%s' % (time_log, action, amount))
            transaction_log.info('%s action: %s  amount: 和和%s', user_info['id'], action, amount)
            account_manage.account_save(user_info, 'common_user')
            return True
