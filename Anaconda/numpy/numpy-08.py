# -*- coding: utf-8 -*-
"""
Created on Mon May 21 22:52:35 2018

数组的对角线
@author: djf
"""

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print(a.diagonal())  #获取对角线的元素


print(a.diagonal(offset=1))  #可以利用偏移求元素  +表示在主对角线的位置向右偏移  -表示向左偏移

#可以使用花式索引来取得数组的主对角线

i = [0,1,2]
print(a[i,i])  

#可以用来修改主对角线元素的值
a[i,i] = 100

print(a)