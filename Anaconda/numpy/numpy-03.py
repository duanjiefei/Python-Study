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

d = array([[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
          ])
print(d)

print(d[0,3:])  #拿到数组的第一行的第四个及第五个元素

print(d[2:,2:]) #拿到数组的第第四行第四列对应的子元素数组

print(d[3,:])#拿到第三行的元素
print(d[:,3])#拿到第三列的元素

print(d[:,:])#拿到所有元素

print(d[2::2, ::2])#2::2  行 从第三行开始，并且能够被index%2==0的行,其实相当于奇数行
                    #::2  列，所有的列，到那时列的index%2==0 也就是奇数列
                    
"""
切片在内存中是用的是引用机制，而不是重新申请内存
        优点：在数组元素较多时，不会为新数组重新分配内存空间
        缺点：在通过索引改变元素的值时，会改变原数组的值
"""

e=array([1,2,3,8,9])

#f = e[2:]
#print(f) # [3 8 9]
#
#f[0] = 100
#print(f)#[100   8   9]
#
#print(e)#[  1   2 100   8   9]

f = e[2:].copy()  #通过copy(0)方法可以为变量重新分配空间
print(f)# [3 8 9]
f[0] = 100
print(f)#[100   8   9]
print(e)#[1 2 3 8 9]


"""
一维花式索引
"""

g = arange(0,100,5)  #产生一维等差数组
print(g)

indexs = [1,3,7,8]  #指定数组的索引们
print(g[indexs])

from numpy.random import  rand

h = rand(10)
print(h)

j = h > 0.5  #嘚到的是一个布尔形数组
print(j)
print(h[j]) #嘚到数组中大于0.5的元素

"""
二维花式索引
"""

k = array([[1,2,3,4,5],
           [2,3,4,5,6],
           [3,4,5,6,7],
           [4,5,6,7,8]])
print(k[(0,1,2,3),(0,1,2,3)]) #(0,1,2,3),(0,1,2,3)前面为行的索引 后面为列的索引

print(k[1:,1:])#取数组的子块

#where 返回所有非零元素的索引

print(where(k))

print(where(k>5))  #返回所有非零元素>5的索引

