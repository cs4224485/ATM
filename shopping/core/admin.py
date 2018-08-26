# Author: harry.cai
# DATE: 2018/2/1
from shopping.goods_db import goods_manage


def put_on_shelve():
    '''
    管理员上架货物功能
    :return:
    '''
    goods_list =[]
    while True:
        good = {'name': '', 'price': '', 'count': 1}
        goods_name = input('请输入上架物品：')
        if goods_name == 'q':
            break
        goods_price = input('请输入物品价格：')
        good['name'] = goods_name
        good['price'] = goods_price
        goods_list.append(good)
        print(goods_list)
    print(goods_list)
    goods_manage.save_goods(goods_list)


def run():
    ''' 目前只写了一个上架功能 '''
    put_on_shelve()