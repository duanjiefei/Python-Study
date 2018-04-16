#装饰器的结构
import time

def timer(func):
    def wrapper(*args,**kwargs):#args 用来接收元祖  kwargs用来接收字典
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("the function run time is %s" %(end_time-start_time))
    return wrapper;
@timer
def test():
    time.sleep(1)
    print("hello python")

# test = timer(test)
# test()
test()

#@timer == test=timer(test)