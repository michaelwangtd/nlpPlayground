#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:michael    time:

import numpy as np
import index
import json

filePath = index.ROOT_PATH + '/source/' + 'stop_word_zh.json'
fr = open(filePath,'r',encoding='utf-8')
line = fr.readline()
print(type(line),len(line))
swList = json.loads(line)
print(type(swList),len(swList))
print(swList)





# print(np.sin(2*np.pi*np.linspace(0,1,5)))
# print(type(np.sin(2*np.pi*np.linspace(0,1,5))))

# print(type(np.random.normal(0,0.1)))
# print(np.random.normal(0,0.1))

# print(type(np.random.randn(3)))
# print(np.random.randn(3))
# print(np.random.randn(3,1))
# print(np.random.randn(1,3))

# np.append()

# print(np.sqrt(0.1))