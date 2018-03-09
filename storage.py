#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

# 查询已有的全部人及其face信息
def GetAllPersonFaces() :
    conn = MongoClient('192.168.1.200', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.persons
    return my_set.find()

# 新增一个人员的信息
def CreatePerson(arg) :
    conn = MongoClient('192.168.1.200', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.persons

    try:
        my_set.insert(arg)
    except:
        print "Insert failed"
        return -1
    else:
        return 0

# 更新一个人的信息，增加新图片地址和face位置
def UpdatePersonPics(id, pic):
    conn = MongoClient('192.168.1.200', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.persons

    my_set.update({'_id':id},{'$push':{'locations': pic}})

    return 0

# 更新一个人的信息:增加新face地址及128D特征
def UpdatePersonFaces(id, arg):
    conn = MongoClient('192.168.1.200', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.persons

    my_set.update({'_id':id},{'$push':{'heap': arg}})

# 更新姓名、性别、年龄
def UpdatePersonInfo(arg):
    pass

# 删除一个人员信息
def RemovePerson(id):
    conn = MongoClient('192.168.1.200', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    # 使用test_set集合，没有则自动创建
    my_set = db.persons

    my_set.remove({'_id':id})
    return 1

# 删除一个face地址及128D特征
def RemoveFace(arg):
    pass
