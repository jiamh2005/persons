#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

# python的模块可多次调用import，挂载到系统上，运行仅一次
SERVER_ADDRESS = '192.168.31.3'
conn = MongoClient(SERVER_ADDRESS, 27017)
# 连接mydb数据库，没有则自动创建
db = conn.mydb
# 使用test_set集合，没有则自动创建
my_set = db.persons
