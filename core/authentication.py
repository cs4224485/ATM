# Author: harry.cai
# DATE: 2018/1/31
import time
import hashlib
from account import account_manage


def auth(user_data, password):

    if user_data['state'] == 'active':
        expire_time = time.mktime(time.strptime(user_data['expire_date'], '%Y-%m-%d'))
        if time.time() < expire_time:
            passwd_hash = hashlib.md5()
            passwd_hash.update(password.encode('utf8'))
            if passwd_hash.hexdigest() == user_data['password']:
                return True
        else:
            print('账号已过期')
            exit()
    else:
        print('账号已被冻结')
        exit()


def login(func):
    '''
    用户登录装饰器
    :param func:
    :return:
    '''
    def inner(user_state, access_log, *args, **kwargs):
        count = 0
        if not user_state['is_login']:
            while count < 3:
                inp_card_id = input('请输入卡号[q退出]：')
                if inp_card_id == 'q':
                    break
                inp_password = input('请输入密码：')
                user_data = account_manage.account_load(inp_card_id, 'common_user')
                if user_data:
                    user_state['is_login'] = auth(user_data, inp_password)
                    if user_state['is_login']:
                        user_state['user_data'] = user_data
                        func()
                        access_log.info('%s is login' % inp_card_id)
                        return user_state
                    else:
                        print('密码错误！')
                        count += 1
                        access_log.warning('%s try to login, but the password wrong' % inp_card_id)
                    if count == 3:
                        user_data['state'] = 'inactive'
                        account_manage.account_save(user_data, 'common_user')
                        print('由于输入次数过多，账户已被冻结')
                        access_log.info('% has been locked' % inp_card_id)
                        break
                else:
                    print('用户不存在')

        else:
            func(*args, **kwargs)
    return inner
