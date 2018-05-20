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


#数组的连接

h = array([[1,2,3],
           [4,5,6]])

i = array([[7,8,9],
           [10,11,12]])

j = concatenate((h,i))  #数组的拼接  默认是按行进行拼接，也就是axis = 0 按第一维进行拼接

print(j)

k = concatenate((h,i),axis = 1)   #数组的拼接，显示的指明axis = 1 即按列进行拼接，按第二维进行拼接

print(k)

l = vstack((h,i))  #对应的就是按行进行拼接  Vertical 水平的

print(l)

m  = hstack((h,i)) # 对应的就是按照列进行拼接  horical  竖直的

#[[ 1  2  3  7  8  9]
# [ 4  5  6 10 11 12]]

print(m)

o = dstack((h,i))  #?不太明白
print(o)

"""
Flatten 数组
  的用途就是将多维数组转化为一维数组
  
   flatten() 方法返回的是数组的拷贝，修改生成的数组的值，不会改变原数组的值
   falt属性会返回所有元素组成的迭代器，通过迭代器去修改后者会改变前者的值
"""
p  = m.flatten()  #[ 1  2  3  7  8  9  4  5  6 10 11 12]
print(p)

p[5] = 100
print(p)
print(m)


q = m.flat

q[0] = 99

print(q)
print(m)



