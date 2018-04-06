# 字符串格式化
# msg  = 'i am a boy ,my name is %s ' %'djf'
msg = 'i am a %s ,my name is %s' %('boy','djf')
print(msg)
msg = 'i am a %(sex)s,my old is %(old)d' %{"sex":"boy","old":15}#通过KEY VALUE 的形式去传值
print(msg)


tpl  = "i am {},age {},{}".format("djf",28,"from henan")
print(tpl)

tpl  = "i am {2},age {1},{0}".format("djf",28,"from henan")#根据索引去取值
print(tpl)