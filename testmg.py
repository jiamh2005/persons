#!/usr/bin/env python
# -*- coding:utf-8 -*-

from modules.storage.storage import GetAllPersonFaces
from bson.objectid import ObjectId

# 添加多条数据到集合中
persons=[
	{
		"_id": '123',
		"name": "zhangsan",
		"ages": [12,18],
		"gender": "male",
		"locations": [
			{
				"pic": '234',
				"locate": [12,20,11,20]
			},
			{
				"pic": '545',
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
				"pic": '5656',
				"locate": [12,20,11,20]
			},
			{
				"pic": '1123',
				"locate": [120,20,140,20]
			}],
		"heap": [{"url": "http://jia.top/ppp/12333.jpg"}]
	}]

##CreatePerson(persons)

# 查询全部

# RemovePerson(ObjectId('5aa24174c76ac72c545bcf24'))
#UpdatePersonPics('123', {"pic":"1233221", "locate":[12,232,22,11]})
#UpdatePersonFaces('123',{"url":"/1233.png", "descriptor":[12,232,22,11,234,3432234,23423]})
#mydata = GetAllPersonFaces()
mydata = GetAllPersonFaces()
for i in mydata:
    print(i)
