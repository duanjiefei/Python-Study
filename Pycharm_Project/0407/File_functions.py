# f = open('test','r',encoding='utf-8')#得到文件句柄
# #data = f.read()
# # print(data)
#
#
# #文件打开模式 r w a 读 写 追加
# # print(f.readable())
# #print("第一行",f.readline())
# print(f.readlines())
# f.close()


#文件的写操作
# f = open('test1','w',encoding='utf-8')#w 模式，文件存在会清空文件，不存在会新建一个空文件
# f.write("ldd\n")
# f.write("djf\n")
# f.writelines(['ldd\n','djf\n'])#读写出来的文件必须为字符串
#
# f.close()

#文件的追加操作

# f = open('test1','a',encoding='utf-8')
# f.write('\n写在文件最后')

#文件的操作模式
#r+  可读写

src_file = open('test1','r',encoding='utf-8')
data = src_file.readlines()
src_file.close()


des_file = open('des','w',encoding='utf-8')
des_file.writelines(data)
des_file.close()
#打开文件，关闭的操作交由操作系统去做
with open('test','r',encoding='utf-8') as src_f ,open('test123','w',encoding='utf-8') as des_f:
    data = src_f.read()
    des_f.write(data)







