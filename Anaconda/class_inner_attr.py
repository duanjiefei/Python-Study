# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:57:51 2018

@author: Sky000
"""
#class Foo:
#    x = 2
#    def __init__(self,y):
#        self.y = y
#    def __getattr__(self,item):
#        print("__getattr__")  #获取类不存在的属性时会触发这个方法
#    def __delattr__(self,item):
#        print("__delattr__")  #删除类的属性时会触发这个方法
#        self.__dict__.pop(item)
#    def __setattr__(self,key,value):
#        print("__setattr__")  #设置类的属性时会触发这个方法
#        self.__dict__[key] = value

class Foo:
    name = ""
    def __init__(self,name):
        self.name = name
    def __getattr__(self,item):
        print("you are looking for %s attr is not found" %item) 
        
foo = Foo("bread")
print(foo.name)

print(foo.price) #重写了__getattr__之后能够防止报错  如果实例的属性不存在时

# 授权 




