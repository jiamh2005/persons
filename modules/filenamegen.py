#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import random

x="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

#此函数的作用为生成number位不重复的随机字符串，number最大为62
def singlerandom(number):
    stringy=''.join(random.sample(x,number)).replace(' ','')
    return stringy

def nsfile(s):
    '''The number of new expected documents'''
    nsfiles = []
    #生成文件名
    for i in range(1,s+1):
        localTime = time.strftime("%Y%m%d%H%M%S",time.localtime())
        localNum = singlerandom(6)
        #print localtime
        filename = localTime + localNum
        nsfiles.append(filename)
    return nsfiles


def file_extension(path):
    return os.path.splitext(path)[1]

def file_dir(path):
    path = path.replace("\\","/")
    return os.path.split(path)[0]

def file_name(path):
    filename = os.path.split(path)[1]
    return os.path.splitext(filename)[0]

if __name__ == '__main__':
    s = input("Please input number of files:")
    print nsfile(s)
