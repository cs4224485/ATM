# Author: harry.cai
# DATE: 2018/2/1
import os
import json

from shopping.setting import config


def save_goods(goods):
    file_name = os.path.join(config.GOODS_DB_PATH)
    json.dump(goods, open(file_name, 'w'))


def load_goods():
    file_name = os.path.join(config.GOODS_DB_PATH)
    goods = json.load(open(file_name, 'r'))
    return goods