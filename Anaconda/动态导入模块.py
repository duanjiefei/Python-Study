# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:27:55 2018

@author: Sky000
"""

#from modlue import test
#
#test.test1()
#test.test2()
#
#modlue_test = __import__("modlue.test")
#print(modlue_test)
#modlue_test.test.test1()
#
#
#m = __import__("Hello_Anaconda")
#print(m)

#from modlue.test import *
#
#test1()
#test2()

import importlib
m = importlib.import_module("modlue.test")
m.test1()
print(m)

#modlue_test = __import__("modlue.test")
#print(modlue_test)
#modlue_test.test.test1()  注意与上面使用importlib的区别