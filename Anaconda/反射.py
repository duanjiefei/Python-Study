# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:52:20 2018

@author: jiefeiduan
"""

class BlackMedium:
        feature = "ugly"
        def __init__(self,name,adder):
            self.name = name
            self.adder = adder
        def sell_house(self):
            print("%s 正在卖房子" % self.name)
        def rent_house(self):
            print("%s 正在租房子" % self.name)
            
bl = BlackMedium("房东","应人石")
bl.sell_house()


def func():
        print("add a function")

rent = getattr(bl,"rent_house")  #通过getattr 可以通过对象拿到对象的方法
rent()
print(bl.name)
setattr(bl,"name","duanjiefei") #通过setattr 可以通过对象去修改对象的属性和方法
print(bl.name)

setattr(bl,"function",func)  #通过setattr 可以通过对象去修改对象的属性和方法
bl.function()
print(bl.__dict__)


