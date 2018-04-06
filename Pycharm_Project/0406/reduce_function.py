from functools import reduce
num = [1,3,5]


def reduce_test(array):
    res = 0
    for n in array:
        res+=n
    return res

print(reduce_test(num))

#reduce 函数的功能：把所有的列表数值合并为一个具体的值
# map 函数的功能：把所有的列表的每一个元素，做某种运算，生成一个新的列表，列表元素个数不变
#filter 函数的功能 ：把列表的元素进行筛选，生成一个新的列表


reduce(lambda x,y:x+y,num,100)#指定一个初始值