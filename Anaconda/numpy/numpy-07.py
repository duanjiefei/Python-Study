# -*- coding: utf-8 -*-
"""
Created on Tue May 15 23:39:46 2018


数组的形状
@author: djf
"""

from numpy import *

a = arange(6)
print(a)
a.shape = 2,3  #修改数组的形状，将数组修改为，2行 3列 》》shape方法会改变原来数组的值
print(a)

b = a.reshape(3,2)  #reshape 方法不会改变原来数组的值
print(b)
print(a)


# shape和reshape 方法不允许该改变元素的总数，否则会报错


#数组的转置


c = array([[1,2,3],
           [4,5,6],
           [7,8,9]])

d = c.transpose()  #求数组的转置
print(d)
e = d.T #T同样可以求数组的转置
print(e)

f = arange(60)

print(f)
f.shape = 12,5
print(f)

g = f.T
g[0,5] = 99  #修改数组的值不仅会改变数组的转置的值，也会改变原数组的值
print(g)
print(f)


