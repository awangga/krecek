#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:50:22 2019

@author: awangga
"""

import h5py
#import numpy

def getList(filename):
    data = h5py.File(filename)
    return list(data.keys())

def getRaw(filename):
    data = h5py.File(filename)
    return data

def getData(filename,listname):
    with h5py.File(filename, 'r') as f:
        my_array = f[listname][()]
    return my_array