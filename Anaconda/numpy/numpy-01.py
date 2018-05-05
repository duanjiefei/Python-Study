# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:33:51 2018

@author: Sky000
"""

#### numpy简介######
from  numpy import *
import matplotlib.pyplot as plt
l = [1,2,3,4,5,6]

print(l)

a  = array(l)
print(a)

b = a + 1
print(b)

print(a+b)

print(a[0])  #获取数组的某个元素


print(a[:2])  #获取数组的前两个元素
print(b[-2:]) #获取数组的后两个元素

print(a[:2] + b[-2:]) #将数组的元素相加

print(a.shape)  #获取数组的维数

a.shape = 2,3  #将a更改为2行3列
print(a)

print(a+a) #a已经变为了对维数组
print(a*a) #数组的相乘，依然是对应位置的元素相乘，而不是矩阵的相乘
#linspace 用于生成等间距的元素  在0~15之间生成3个元素使之间距相等
c = linspace(0,15,3)  
print(c)

e = linspace(0,2*pi,25)  #将0——2*pi  分为24分，即每份代表15度
print(e)
d = sin(e)  #对每一度求正弦
print(d)

plt.plot(e,d)  #将e的元素作为x轴，d的元素作为y轴，进行画图
plt.show()






