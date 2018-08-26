# Author: harry.cai
# DATE: 2018/1/31

import random
import datetime
from account import account_manage
import hashlib

class admin_action:
    '''
    管理员相关操作
    '''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_state = False

    @staticmethod
    def loin_auth(username, password, obj):
        if username == obj.username  and password == obj.password:
            obj.login_state = True
        else:
            print('用户名或密码错误')

    @staticmethod
    def create_user():
        '''
        建立用户信息
        :return:
        '''

        # 生成创建时间和到期时间
        date = datetime.datetime.now()
        create_date = '%s-%s-%s' % (date.year, date.month, date.day)
        end_time = date.replace(date.year + 10)
        expire_date = '%s-%s-%s' % (end_time.year, end_time.month, end_time.day)

        # 生成随机ID
        number = []
        for i in range(10):
            num = str(random.randint(0, 9))
            number.append(num)
        number = ''.join(number)

        passwd = input('请设置密码：')
        md5_obj = hashlib.md5()
        md5_obj.update(bytes(passwd, encoding='utf8'))

        user_data = {
            'id': number,
            'password': md5_obj.hexdigest(),   # 初始化密码
            'create_date': create_date,
            'expire_date': expire_date,
            'credit_limit': 15000,
            'balance': 15000,
            'history_list': [],
            'state': 'active'
        }

        # 存储用户信息
        is_saved = account_manage.account_save(user_data, 'common_user')
        if is_saved:
            print('用户创建成功')

    @staticmethod
    def freeze():
        """ 冻结账户 """
        card_id = input('请输入用冻结的id:')
        user_data = account_manage.account_load(card_id.strip(), 'common_user')
        if user_data:
            user_data['state'] = 'inactive'
            account_manage.account_save(user_data, 'common_user')
            print('用户已被冻结')
        else:
            print('用户不存在')

    @staticmethod
    def change_credit():
        ''' 调整信用额度 '''
        card_id = input('请输入要修改的ID：')
        change_amount = input('请输入要增加的金额：')
        user_data = account_manage.account_load(card_id.strip(), 'common_user')
        if user_data:
            user_data['credit_limit'] += int(change_amount)
            user_data['balance'] += int(change_amount)
            account_manage.account_save(user_data, 'common_user')
            print('修改成功！')
        else:
            print('用户不存在')


def interactive():
    menu = '''
         --------- admin mode -----------
                1 创建用户
                2 冻结用户
                3 调整额度

        '''
    dic_menu = {
        '1': admin_action.create_user,
        '2': admin_action.freeze,
        '3': admin_action.change_credit
    }
    while True:
        print(menu)
        choice = input('>>>')
        if choice in dic_menu:
            dic_menu[choice]()


def admin_interface():
    ''' 管理员接口 '''
    inp_username = input('请输入用户名：')
    inp_password = input('请输入密码：')
    admin_obj = account_manage.account_load(inp_username, 'admin')
    if admin_obj:
        admin_action.loin_auth(inp_username, inp_password, admin_obj)
        if admin_obj.login_state:
            interactive()
    else:
        print('管理员账户不存在')