#map函数
# def inc(i):
#     return i+1
# def dec(i):
#     return i-1


# def map_test(func, array):
#     ret = []
#     for i in array:
#         res = func(i)
#         ret.append(res)
#     return ret
# map_test(lambda x:x + 1,num_l)
num_l = [13,4]
res = map(lambda x:x+1,num_l)
print(list(res))


