#函数的学习
# def test(x):
#     y = 2*x + 1
#     return y
#
#
# print(test(5))

#过程就是没有return 的函数


# **字典  *列表
# def test(x,*args):
#     print(x)
#     print(args)
#
# test(1,2,3,4,5,6)#输出时第二个元素回座位元祖来输出
# test(1,[2,3,4,5,6])#此时列表是作为一个整体的单独元素，即列表是一个整体的，是一个元祖元素
# test(1,[2,3,4,5,6],[2,3,4,5])
# test(1,*[2,3,4,5])#此时列表中的每一个元素都会被当做一个元祖来对待
# test(1,{"key":"value"})


# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
#
# test(1,y = 2 ,z = 3)#输出会以字典的形式输出

# def test(x,*args,**kwargs):
#     print(x)
#     print(args) #输出位置参数
#     print(kwargs)#输出关键字参数
#
# test(1,*[1,2,3],**{"key":"value"}) ##位置参数必须在关键字参数之前传递
# 无声明局部变量  ：
#全局变量与局部变量的命名规则  建议全局变量大写  局部变量小写
# global 全局变量 nolocal 上一级变量
# name  = "djf"
# def test():
#
#     global  name  #可以通过global 关键字获取全局变量
#     name  = "ldd"
#     print(name)
#
# test()

#匿名函数

def calc(x):
    return x + 1

print(calc(5))

lambda x:x+1
func = lambda x:x+1
print(func(10))

# 面向过程 函数式编程 面向对象
#函数式编程 = 编程语言定义的函数 + 数学意义的函数
