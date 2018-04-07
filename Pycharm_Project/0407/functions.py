#zip函数
ret = zip(('a','a','c'),(1,2,3))
print(list(ret))#zip函数会将对应的元祖（序列类型的元素）进行key value形式进行对应


age_dic = {'age1':20,'age2':30,'age3':40}
#max函数
print(max(age_dic.values()))
print(max(age_dic))
ret = zip(age_dic.values(),age_dic.keys())
print(list(max(ret)))



#min函数

#ord函数
print(ord('a'))

#pow函数
print(pow(10,3))#10*10*10
print(pow(10,3,2))#10*10*10 对2取余

#reversied反转函数

#slice切片

#sorted 排序

