#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from pymongo import MongoClient
from conn import my_set

# 查询已有的全部人及其face信息
def GetAllPersonFaces() :
    return my_set.find()

# 新增一个人员的信息
def CreatePerson(arg) :
    try:
        my_set.insert(arg)
    except:
        print "Insert failed"
        return -1
    else:
        return 0

# 更新一个人的信息，增加新图片地址和face位置
def UpdatePersonPics(id, pic):
    my_set.update({'_id':id},{'$push':{'locations': pic}})
    return 0

# 更新一个人的信息:增加新face地址及128D特征
def UpdatePersonFaces(id, arg):
    my_set.update({'_id':id},{'$push':{'heap': arg}})

# 更新姓名、性别、年龄
def UpdatePersonInfo(arg):
    pass

# 删除一个人员信息
def RemovePerson(id):
    my_set.remove({'_id':id})
    return 1

# 删除一个face地址及128D特征
def RemoveFace(arg):
    pass

def SaveFace(filepath, descriptor):
    #person = {
	#	"name": "none",
	#	"ages": [0],
	#	"gender": "unknown",
    #}
    #person['_id'] = '123'
    #person['locations'] = []
    print filepath
    pass

def SaveImage(filepath, locations) :
    #pic = {
	#	"desc": "none",
    #}
    #pic['_id'] = '123'
    #pic['locations'] = []
    print filepath
    print locations
    pass

def face_distance(face_encodings, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.
    :param faces: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A numpy ndarray with the distance for each face in the same order as the 'faces' array
    """
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)
