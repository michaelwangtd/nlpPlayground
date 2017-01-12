#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:michael

import numpy as np
from scipy.optimize import leastsq
import pylab as pl

"""
    python realize least square
"""

def getPoly(factor,x):
    f = np.poly1d(factor)
    return f(x)

def getResidual(factor,x,y):
    regularization = 0.00000001
    ret = getPoly(factor,x) - y
    # ret = np.append(ret,np.sqrt(regularization) * factor)
    return ret

if __name__ == '__main__':
    # 多项式次数
    polyNum = 9
    # 样本x
    sampleX = np.linspace(0,1,9)
    # X轨迹
    traceX = np.linspace(0,1,1000)
    # 样本y
    sampleY = np.sin(2 * np.pi * sampleX)
    # 实际y
    realY = [np.random.normal(0,0.1) + y for y in sampleY]
    # 随机系数
    randomFactor = np.random.randn(polyNum)
    # 拟合的参数
    fitFactor = leastsq(getResidual,randomFactor,args=(realY,sampleX))
    print('拟合的参数:',fitFactor[0])
    # 输出
    pl.plot(traceX,np.sin(2*np.pi*traceX),label='real')
    pl.plot(traceX,getPoly(fitFactor[0],traceX),label='fited')
    pl.plot(sampleX,realY,'bo',label='noise')
    pl.legend()
    pl.show()


