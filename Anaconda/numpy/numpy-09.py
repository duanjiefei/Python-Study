# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:12:31 2018

数组与字符串的转化
@author: djf
"""

import numpy as np

a =  np.array([[1,2],[3,4]],dtype = np.uint8)

print(a)

print(a.tostring()) #'\x01\x02\x03\x04'

s = a.tostring()

l = np.fromstring(s,dtype = np.uint8)

print(l)

l.shape = 2,2
print(l)

