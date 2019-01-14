
import re


#  要求是@ 前面是4位到20位,的163邮箱(@163.com)



match_str = "[a-zA-Z_0-9]{4,20}@163\.com$"

while True:
    print("Start")
    mail = input("请输入邮箱:")
    res = re.match(match_str,mail)

    if res:
        print("%s 是163邮箱" % mail)
        print("Yes")
    else:
        print("%s 不是163邮箱格式" % mail)
        print("NO")