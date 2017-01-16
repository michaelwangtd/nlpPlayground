#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,util
from modules import nlp

"""

"""

if __name__ == '__main__':
    # 文件路径
    stopWordFilePath = io.getSourceFilePath('stop_word_zh.json')

    stopWordList = nlp.getStopWordList('stop_word_zh.json')
    print(stopWordList)
