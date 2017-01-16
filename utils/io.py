#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: michael

import os
import index

"""
    输入/输出流处理的工具文件
"""

def getOneFromTxt(filePath):
    '''
        从文本文件中获取内容并返回
        适用于文本文件只有一条记录的情况
        因为是一条记录数据，所以不用list进行存储
    '''
    if os.path.exists(filePath):
        fr = open(filePath,'r',encoding='utf-8')
        one = fr.readline()
        return one
    else:
        print('getOneFromTxt()文件不存在')


def getSourceFilePath(fileName):
    '''
        根据fileName获取“Source”目录下文件路径
    '''
    return os.path.join(index.ROOT_PATH,index.DIR_SOURCE,fileName)

