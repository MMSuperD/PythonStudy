import re

# 注意点 . 字符(不包括\n) 匹配任意一个字符的时候,我们如果要匹配 换行(\n),我们需要在match函数中添加第三个参数re.S (列子:match(正则表达式,匹配的内容,re.S))

# ? 表示问好前面的字符可以有也可以没有

# res = re.match(r"hello?\d{0,4}","hello12132")
#
# print(res.group())

#需求:匹配出变量名是否有效

names = ["name1","_name","2_name","__name"]

match_string = "[a-zA-Z_]+(\w)*"

for name in names:
    ret = re.match(match_string,name)

    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 不符合要求" % name)