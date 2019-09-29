import re


re_str = "[a-zA-Z_]{4,20}@163\.com$"

while True:

    input_content = input("请输入邮箱:")
    result = re.match(re_str, input_content)

    if result:
        print(input_content,"符合要求")
    else:
        print(input_content, "不符合要求")


