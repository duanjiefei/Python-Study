#装饰器的原则
# 1 不修改函数内部的源代码
# 2 不修改函数的调用方式
#装饰器 = 高阶函数 函数嵌套 闭包
#高阶函数： 函数的参数是函数名  函数的返回值是函数名

import time
def foo():
    time.sleep(1)
    print("hello python")


# 多运行了一次
# def test(func):
#     print(func)
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print("the function sleep time %s"%(stop_time-start_time))
#     return func

def test(func):
    print(func)
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the function sleep time %s"%(stop_time-start_time))
    return func
foo = test(foo)
foo()

#函数嵌套  ： 在函数内部定义另一个函数
#闭包




