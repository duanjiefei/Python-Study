# -*- coding: utf-8 -*-
"""
Created on Sat May 12 00:36:46 2018
数组的排序  
@author: djf
"""
from numpy import *
#数组函数
names = array(["duanjiefei","liudandan","duanjiehao"])
weights = array([70,50,45])

sort_weights = sort(weights) #sort 函数会将数组的元素进行排序
print(sort_weights)  #[45 50 70]
print(weights)  #sort函数并不改变原来数组元素的值


indexs = argsort(weights)
print(indexs)#[45 50 70] argsort函数返回，从小到大排序后的数组在原数组的位置索引

#可以用生成的索引数组取访问对应的元素
print(weights[indexs])


#使用函数并不会改变原来数组的值
"""

        数组方法

"""
#weights.sort()
print(weights)  #使用方法也可以对元素进行排序，但是会改变原来数组的值

indexs_w = weights.argsort()
print(indexs_w) #使用该方法同样可以返回从小到大排序后的数组在原数组的索引

"""

        二维数组的排序

"""

percent = array([[0.2,0.1,0.3,0.5],
                 [0.3,0.9,0.6,0.7],
                 [0.1,0.7,0.5,0.6],
                 ])
print(percent)  
print(sort(percent)) #默认对每一行进行排序


print(sort(percent,axis = 0))  #对每一列进行排序

"""

        searchsorted 函数的使用

"""

sorted_array = linspace(0,1,10)
print(sorted_array)

insert_array = array([0.53,0.89])
index_array = searchsorted(sorted_array,insert_array)
print(index_array)  # searchsorted 函数会将后者的元素插入到前者的数组中，并返回插入元素位置的索引

print(sorted_array[index_array[0]:index_array[1]])  #将介于两者之间的元素进行获取
