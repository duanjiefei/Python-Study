import re
# ..  通配符  一个点代表匹配一个任意元素    加上？ 会将贪婪匹配改为惰性匹配
#  a$   以元素a为结束标志
#  ^a    以a元素开始为标志
# *  匹配  (0   +00无穷)   贪婪匹配  会以结束元素的最多次数进行匹配
# +  匹配   （1    +00无穷）会以结束元素的最多次数进行匹配
# ?  匹配    （0   1）会以结束元素的最多次数进行匹配
# {}  自定义元素的匹配个数  {0，} == *  {1，}== +  {0,1} == ？ {6} == 重复元素6次
#[字符集]   q[^a-z]  匹配非小写字母  特殊符号 - ^  \
# \  \反斜杠后面跟元字符去除元字符的特殊功能
    # \ 反斜杠后面跟普通字符，实现特殊功能
    # \d 匹配任何十进制数
    # \D 匹配任何非数字字符
    # \s 匹配任何空白字符
    # \S 匹配任何非空白字符
    # \w 匹配任何字母数字字符
    # \W 匹配任何非字母数字字符
    # \b 匹配一个特殊字符边界
# （）分组
 # result = re.findall("d*","ddddd")   # 贪婪匹配，会以最多的d得个数为匹配
result = re.findall("alex*","adddfffffale")
print(result)
result = re.findall("alex+","adddfffffale")
print(result)
result = re.findall("alex?","adddfffffalexxxx")
print(result)
result = re.findall("\([^()]*\)","12+(34*6+4*3+(3-1))")
print(result)