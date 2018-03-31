# 元祖 tuple ()  不可修改，不能增加与删除
# 列表 list []
# 推荐在写元祖的最后加一个
tu = (111,2222,333)
v = tu[0]#索引
print(v)
v1 = tu[0:1] # 切片
print(v1)
for v2 in tu:#支持for循环
    print(v2)

s = "duanjiefei"
v3 = tuple(s)#转换
print(v3)
s1 = ("duanjiefei","liudandan")
v4 = "_".join(s1)#插入
print(v4)
#元祖也是有序的，元祖的一级元素不可修改，如果元组的一级元素可以被修改，则内容可以被修改

#count 计算某个元素出现的次数
#index 查找某个元素的索引

#字典

info = {"k1":"v1",
        "k2":"v2"}
#字典是通过键值对的形式表示的

# dict 字典  {key : value ,key : value ..........}

info = {"k1":1,
        "k2":True,
        "k3":[
            11,
            22,
            "duanjiefie"
        ]
}

# value 可以实任意类型, 列表不能作为字典的key, 元祖可以作为字典的key，字典不可以作为字典的key ,布尔值可以作为字典的key，按1 0来转化为key
print(info)
print(info)
print(info)
print(info)
print(info)
print(info)
# dict 内部是通过哈希值进行存储的，列表不支持哈希的转化
# 字典是无序的 每次的打印值是不确定的
print(info["k1"])

del info["k2"] #删除
print(info)

for item in info:
    print (item)  #默认的for循环只有key

for item in info.keys():
    print (item)
for item in info.values():
    print(item)

for k,v in info.items(): #key value 可以同时被打印
    print(k,v)
# dict的方法  fromkeys
dic = dict.fromkeys(["duan","jie","fei"],"liu")
print(dic) #根据key值去创建 字典

print(dic.get("duan")) #根据key 去获取value的值

#pop
dic1 = dic.pop("duan")  #返回value
print(dic1)

dic2 = dic.popitem()
print(dic2)  #随机返回一个item

#setdefault  设置值
# 1 当key存在时，不设置，返回当前key对应的value
# 2 当key不存在时，设置，将对应的key 和 value进行插入
dic3 = dic.setdefault("duan","dandan")
print(dic3)

#update 对字典对应的值进行更新


# 1 整数int
# 2字符串
# replace find join strip startswith endswith split upper lower format
#3 列表
# append extend insert
# 索引 切片 循环
# 4 元祖
#索引 切片 循环  一级元素不可被修改
# 5 字典
# get update keys values items
# 循环 索引
# 6 布尔值
# None "" () [] {} 0 >>>>>>>false