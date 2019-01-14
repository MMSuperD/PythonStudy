
import re

#正则表达式在匹配字符串的时候,如果匹配到字符串,就返回结果,如果没有匹配到字符串就不返回结果


#1.这个是第一种匹配单个字符
# res = re.match(r"[hH]ello","Hello world you")
# 
# res.group()
# 
# print(res.group())


#2.这个也是单个字符匹配
# res = re.match(r"[1-8]mmd","3mmdsfdkkfjsdlfks")
#
# res.group()
#
# print(res.group())

#3.这个也是单个字符匹配
res = re.match(r"[1-8]mmd","9mmdsfdkkfjsdlfks")

if res not NoneType :
    print(res.group())


