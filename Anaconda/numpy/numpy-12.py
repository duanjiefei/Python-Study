# -*- coding: utf-8 -*-
"""
Created on Sun May 27 20:29:46 2018
数组转化为矩阵
@author: djf
"""

import numpy as np


a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a)

A = np.mat(a)  #将数组转化为矩阵
print(A)

B = np.mat("1,2,3;4,5,6;7,8,10") #将字符串转为数组
print(B)

C = np.bmat("A,B;B,A")  #利用bmat可以将分块矩阵转化为整合矩阵
print(C)

x = np.array([[1],[2],[3]])
print(A*x)  #矩阵的相乘

print(A.I)
print(A*A.I)

D = np.mat("1,0,0;0,1,0;0,0,1")
print(D)

print(D.I)

print(D*D.I)

print(D**4) #矩阵的幂