# -*- coding: utf-8 -*-
"""
Created on Sat May 12 00:14:23 2018

数组方法
@author: djf
"""

from numpy import *
a = array([[1,2,3],
           [1,2,3]])
print(sum(a))  #对数组的所有元素求和

print(sum(a,axis=0)) #沿着一维求和  [2 4 6]
print(sum(a,axis=1)) #沿着二维求和 [6 6]

##求积

print(prod(a,axis=0))#[1 4 9]
print(prod(a,axis=1))#[6 6]

