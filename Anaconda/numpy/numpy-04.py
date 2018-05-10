# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:06:49 2018

数组类型

@author: duanjiefei
"""
from numpy import *

"""
复数数组
"""
a = array([1+2j,3,4,5])
print(a)
print(a.real) #查看数组的实部  [1. 3. 4. 5.]
print(a.imag) # 查看数组的虚部[2. 0. 0. 0.]
print(a.dtype) #查看数组的类型 complex128

a.real = [2,5,8,9] #修改数组的虚部
a.imag = [2,5,8,9]#修改数组的虚部
print(a)
print(a.conj())  #查看数组元素的共轭

"""
实际上以上方法可以用于整形数组、浮点数组等
"""
b = array([1,2.0,3,4])
print(b)
print(b.dtype)#float64 默认创建数组为浮点64位
print(b.nbytes)# 8 bit * 4

#当然我们也可以在创建的时候显式的声明要创建的数组的类型
c = array([1,2,3,4],dtype="float32")
print(c)
print(c.dtype)

#可以从二进制数据中读取

d = array([1,2,3,4],dtype=uint8)

d.tofile("d.bat")  #写入数据

#e = frombuffer('d.bat',dtype=uint8)  #读出时报错
#print(e)

import os
os.remove("d.bat")  #清除文件

print(ord('a')) #ord() 读取字符的assic码
"""
#numpy的数据类型

基本类型	可用的Numpy类型	备注
布尔型	bool	占1个字节
整型	int8, int16, int32, int64, int128, int	int 跟C语言中的 long 一样大
无符号整型	uint8, uint16, uint32, uint64, uint128, uint	uint 跟C语言中的 unsigned long 一样大
浮点数	float16, float32, float64, float, longfloat	默认为双精度 float64 ，longfloat 精度大小与系统有关
复数	complex64, complex128, complex, longcomplex	默认为 complex128 ，即实部虚部都为双精度
字符串	string, unicode	可以使用 dtype=S4 表示一个4字节字符串的数组
对象	object	数组中可以使用任意值
Records	void	
时间	datetime64, timedelta64
"""
#python数组的类型可以为任意类型

e = array([1,2.2,"abs",3+3j,[1,2,3]],dtype=object)
print(e)

print(e*2)#[2 4.4 'absabs' (6+6j) list([1, 2, 3, 1, 2, 3])]

#asarray函数不会修改数组原来的值

f = array([1,2.3],dtype=float64)
print(f)
g = asarray(f,dtype = float32)
print(g)
print(g.dtype)#float32
print(f.dtype)#float64  数组的类型及元素不会被修改

h = asarray(g,dtype=float32) #但是当要生成的元素的类型与原来数组的类型一致时，不会分配新的内存空间，而是持有原来数组的引用
print(h is g)#True

#astype 函数也不会改变数组的值，但是会重新分配空间生成新的数组

i = h.astype(float64)
print(i)
print(i.dtype)
print(i is h) #False

j = h.astype(float32)
print(j is h) #FALSE  即astype总是生成一个新的数组，即使类型完全一样


#view方法没搞懂

