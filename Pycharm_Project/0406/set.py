# s = set('hello')
# print(s)
#
# #set 元素不可重复  用{} 表示 ，不同于字典的{key:value,key:value}的形式
# s = set(["alex",'alex','djf'])
# print (s)

# s = {1,2,23,4}
# s.add(4)##只有当元素不同时，才能添加进集合中
# print(s)
#
# s.clear()##清空元素
# print(s)

# s.pop()##清空其中的一个元素，随机删除
# s.remove(23)##制定删除其中一个元素，元素不存在时，无法进行删除，会报错
# s.discard(233)#指定删除，但是元素不存在，也不会报错
# print(s)

#集合的运算  交集 并集

# python_l = ['djf','ldd','djh']
# linux_l = ['djf','anxiao']
#
# p_s =set(python_l)
# l_s = set(linux_l)
# print(p_s)
# print(l_s)
#
# print(p_s.intersection(l_s))#交集  符号 &
# print(p_s.union(l_s))#并集    符号 |
# print(p_s-l_s)  #差集
# print(p_s.difference(l_s)) # 差集
# # 交叉补集
# print(p_s.symmetric_difference(l_s)) #符号^
# s = {1,2}
# b = {3,4}

# print(s.isdisjoint(b))#不存在交集
s = {1,2,3,4}
b = {1,2,3}
print(s.issuperset(b))  #父集
print(b.issubset(s))  #子集
b.update(s)  #求并集，并重新赋值
print(b)


s  = frozenset("hello")  #不可变集合
