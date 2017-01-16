#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,util

"""
    nlp模块：nlp相关功能的实现
"""

def getStopWordList(fileName):
    '''
        fileName: 停用词文件名
        ?? 可以扩展为列表形式
    '''
    filePath = io.getSourceFilePath(fileName)
    content = io.getOneFromTxt(filePath)
    stopWordList = util.jsonLoads(content)
    return stopWordList