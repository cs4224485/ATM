# Author: harry.cai
# DATE: 2018/2/1
import os
import json
from shopping.setting import config
from shopping.user_db import account
from shopping.core import auth
from shopping.goods_db import goods_manage
from core.main import consume

user_info = {
    'is_authentication': False,
    'user_data': None
}


def register():
    ''' 用户账号注册 '''
    username = input('请输入用户名：')
    password = input('请输入密码：')
    user_data = {
        'username': username,
        'password': password,
        'shopping_car': [],
        'history_list': []
    }
    file_name = os.path.join(config.USER_DB_PATH, username)
    if os.path.exists(file_name):
        print('用户名已存在')
    else:
        is_saved = account.save_info(user_data)
        if is_saved:
            print('注册成功！')


def show_goods(user_data):
    ''' 显示商品信息 '''
    goods = goods_manage.load_goods()
    banner = 'SHOPPING'
    print(banner.center(30, '-'))
    for index,g in enumerate(goods):
        print(index, g['name'], g['price'])
    return goods


def shopping(user_data):
    goods = show_goods(user_data)
    while True:
        choice = input('请选择要购买的商品：')
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods):
                if goods[choice] in user_data['shopping_car'] :
                    index = user_data['shopping_car'].index(goods[choice])
                    user_data['shopping_car'][index]['count'] += 1

                else:
                    user_data['shopping_car'].append(goods[choice])
                print('\033[32m%s 已加入购物车 价格：%s\033[0m' % (goods[choice]['name'],goods[choice]['price']))

            else:
                print('\033[31m没有该商品\033[0m')
        if choice == 'b':
            break


def pay_for(user_data):
    banner = 'shopping list'
    print(banner.center(30, '-'))
    total = 0
    for index,good in enumerate(user_data['shopping_car']):
        print(index, good['name'], int(good['price']) * good['count'], good['count'])
        total += int(good['price']) * good['count']

    confirm = input('\033[31m总共消费%s，是否要继续买单[Y/N]:\033[0m' %total)
    if confirm == 'Y':
        pay_for_state = consume(str(total))
        if pay_for_state is not True:
            print('支付失败')
        else:
            user_data['shopping_car'] = None


def interactive(user_data):
    menu='''
    -------- shopping ---------
      1  查看商品
      2  购买商品
      3  结账
    '''
    menu_dic = {
        '1': show_goods,
        '2': shopping,
        '3': pay_for
    }
    while True:
        print(menu)
        choice = input('>>>')
        if choice in menu_dic:
            menu_dic[choice](user_data)


def run():
    menu = ' 1  登录\n 2  注册'
    while True:
        print(menu)
        choice = input('>>>[q退出】:')
        if choice == '1':
            after_auth_data =  auth.login(user_info)
            if after_auth_data:
                interactive(after_auth_data['user_data'])
        elif choice == '2':
            register()
        elif choice == 'q':
            break
        else:
            print('输入有误')