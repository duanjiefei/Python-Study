# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:59:02 2018

numpy 数组及其索引

@author: Administrator
"""



from numpy import *

list_1 = [1,2,3,4]
array_1= array(list_1)  #将列表转为数组
print(array_1)

type_array = type(array_1)
print(type_array)   #<class 'numpy.ndarray'>

array_dtype = array_1.dtype

print(array_dtype) #int32


print(array_1.itemsize)  # 4 

print(array_1.shape)   #(4,) 查看数组的维数

print(array_1.size)  # 查看数组元素的个数   

print(array_1.nbytes)  # 查看所有元素所占的空间  16

print(array_1.ndim)  #查看数组的维数  1

array_1.fill(-4.8)  #将数组设为指定值

print(array_1)


b = array([11,13,15,17,19])
print(b[1:3])  #获取数组的 坐标为[1, 3)区间上的元素

print(b[1:-1])  #区间为[1,-1)  其中-1 代表最后一个元素的索引

print(b[::3])  #index%3 ==0 

print(b[-2:])  #索引为（-2,无穷）

print(b[1:])
print(b[:-1])
print(b[1:]-b[:-1])  #用于计算数组相邻两个元素的差


#多维数组及其属性
c = array([[1,2,3,4],[5,6,7,8]])
print(c)

print(c.shape)#(2, 4)  2行4列
 
print(c.size) #查看数组元素的个数 8

print(c.ndim) #查看数组元素的维数  2

print(c[1,3]) #1 代表第二行 3代表第四列

print(c[1]) #代表元素的第二列