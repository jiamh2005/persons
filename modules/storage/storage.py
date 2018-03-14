#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from pymongo import MongoClient
from myconn import my_pics,my_persons
from modules.filenamegen import file_name
from modules.face import face_distance

# 查询已有的全部人及其face信息
def GetAllPersonFaces() :
    return my_persons.find()

# 新增一个人员的信息
def CreatePerson(arg) :
    my_persons.insert(arg)


# 更新一个人的信息，增加新图片地址和face位置
def UpdatePersonPics(id, pic):
    my_persons.update({'_id':id},{'$push':{'locations': pic}})
    return 0

# 更新一个人的信息:增加新face地址及128D特征
def UpdatePersonFaces(id, facepath, descriptor):
    my_persons.update({'_id':id},{'$push':{'faces': facepath}})
    my_persons.update({'_id':id},{'$push':{'descriptors': descriptor}})
# 更新姓名、性别、年龄
def UpdatePersonInfo(arg):
    pass

# 删除一个人员信息
def RemovePerson(id):
    my_persons.remove({'_id':id})
    return 1

# 删除一个face地址及128D特征
def RemoveFace(arg):
    pass

def SavePerson(imgpath,facepath,descriptor):
    person = {
		"name": "none",
		"ages": [0],
		"gender": "unknown",
        "pics": [],
        "faces": [],
        "descriptors": []
    }
    person['pics'].append(imgpath)
    person['faces'].append(facepath)
    person['descriptors'].append(descriptor)

    my_persons.insert(person)

def SaveFace(facepath, descriptor,imgpath):
    allpersons = GetAllPersonFaces()
    found = False
    same = False
    position = 0
    for p in allpersons :
        if p.has_key('descriptors') :
            min_d = 1
            for d in p['descriptors'] :
                fd = face_distance(descriptor, d)
                if fd < min_d:
                    min_d = fd;

            if min_d < 0.44 :
                print fd
                print facepath
                print p["faces"]
                position = p
                found = True
                if fd < 0.2 :
                    same = True
        if found :
            break

    if found :
        UpdatePersonPics(position['_id'], imgpath)
        if not same :
            UpdatePersonFaces(position['_id'],facepath, descriptor)
    else:
        SavePerson(imgpath,facepath,descriptor)


def SaveImage(filepath, locations) :
    pic = {
		"desc": "none",
        "name": "blank"
    }
    pic['link'] = file_name(filepath)
    pic['locations'] = locations
    my_pics.insert(pic)
