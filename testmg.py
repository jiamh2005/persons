#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('192.168.1.200', 27017)

# 连接mydb数据库，没有则自动创建
db = conn.mydb

# 使用test_set集合，没有则自动创建
my_set = db.persons

# 添加多条数据到集合中
persons=[
	{
		"name": "zhangsan",
		"ages": [12,18],
		"gender": "male",
		"locations": [
			{
				"url": "http://example.com/pic/001.jpg",
				"locate": [12,20,11,20]
			},
			{
				"url": "http://example.com/pic/002.jpg",
				"locate": [120,20,140,20]
			}],
		"heap": [{"url": "http://jia.top/ppp/03223.jpg"}]
	},
	{
		"name":"lisi",
		"ages": [12,18],
		"gender": "female",
		"locations": [
			{
				"url": "http://example.com/pic/003.jpg",
				"locate": [12,20,11,20]
			},
			{
				"url": "http://example.com/pic/004.jpg",
				"locate": [120,20,140,20]
			}],
		"heap": [{"url": "http://jia.top/ppp/12333.jpg"}]
	}]
	
my_set.insert(persons)

# 查询全部
for i in my_set.find():
    print(i)