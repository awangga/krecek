#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:33:32 2019

@author: awangga
"""


import matlab


filename='./vim2/Stimuli.mat'
data = matlab.getRaw(filename)
x = matlab.getList(filename)
sv= matlab.getData(filename,"sv")
st= matlab.getData(filename,"st")
sv

print(filename)
#x = f["x"]
#x = f["x"]
#numpy.array(x)

x=list(data.keys())
x[0]
a=data[x[0]]
b=data[x[1]]
a[10]
w=data[x[0]][0]
#www=data[data[x[1]]['wave'][0][0]].value