# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:20:14 2018

Matplotlib 基础

@author: Administrator
"""

import  numpy as np 
import matplotlib.pyplot as plt


x = linspace(0,2*pi,25)
print(x)


#plt.plot(sin(x))
#plt.show()   



#plt.plot(x,sin(x))  #以x为横轴，sinx 为纵轴
#plt.show()  #调用一次show方法会生成一个坐标图

#plt.plot(x,sin(x),'b-o',
#         x,sin(2*x),'r-^')  #'b>blue 蓝色 o 圆点'  'r>red 红色 ^ 尖角'

#plt.plot(x,sin(x),'bo',
         #x,sin(2*x),'r^')  #'b>blue   蓝色 o 圆点'  'r>red 红色 ^ 尖角'  -代表连续  没有-代表离散


#plt.scatter(x,sin(x))  #scatter 可以用来画离散图

#x = plt.rand(20)
#y = rand(20)
#size = rand(20)*30
#color = rand(20)
#plt.scatter(x,y,size,color)
#
#colorbar()

#plt.figure()  #figur命令用于生成新的图表
#plt.plot(sin(x))
#plt.figure()
#plt.plot(cos(x))
#plt.hold(True) 
plt.subplot(2,2,1)
plt.plot(tan(x))
plt.subplot(2,2,2)
plt.plot(sin(x))
plt.subplot(2,2,3)
plt.plot(cos(x))   #plt.subplot(2,2,1)  row column index

#plt.plot(sin(x))
##plt.hold(False)  #hold函数已经被废弃
#plt.plot(cos(x))
#plt.hold(True)
plt.figure()
#plt.clf()  清除 关闭图像  clf close close("all")
      
plt.plot(sin(x),'r-o')
plt.plot(cos(x),'b-^')
plt.legend(['sin','cos'])  #legend 为坐标图加上图列

plt.xlabel("x 轴")  
plt.ylabel("y 轴")
plt.title("sin(x) red cos(x) blue")
plt.grid()


#from scipy.misc import lena
#img = lena()
#
#print(img)
 

