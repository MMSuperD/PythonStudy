import re


def 判断变量名是否合法():
    # 判断一个变量名是否合法
    name_list = ["sjfdslfkds", ")dsfsdfs", "_sdfsd56723)", "_dsfsdf2323", "8sdfsf", "sdfs_23"]

    # ^ 以什么开头  $ 以什么结尾 + 至少一个  * 可以为零个

    re_str = "^[_a-zA-Z]+[_a-zA-Z0-9]*$"

    for name in name_list:
        result = re.match(re_str, name)
        if result:
            print(name, "合法")
        else:
            print(name, "不合法")


def 判断是否符合邮箱格式():
    # 判断一个邮箱是否合法
    name_list = ["sjfdslfkds@121.com", "sjfdslfkds@121com", "sjfdslfkds@121.cn",  ")dsfsdfs.com", "_sdfsd56723@.com)", "_dsfsdf2323@12.com", "8sdfsf", "sdfs_23"]

    # ^ 以什么开头  $ 以什么结尾 + 至少一个  * 可以为零个
    # 邮箱条件 1.首先需要 以字母和数字开头 2.中间需要有@  3.需要以.cn 或者 .com 结尾  4. 点这样的字符需要转义

    re_str = "(^[0-9a-zA-Z]+)@([a-zA-Z0-9]+)(\.cn|\.com)$"

    for name in name_list:
        result = re.match(re_str, name)
        if result:
            print(name, "合法")
        else:
            print(name, "不合法")


判断是否符合邮箱格式()

# 判断变量名是否合法()



