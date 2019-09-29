import re


name_list = ["fsdjf", "678fsd", "_sfsf998", "[\]fss", "_sdfsfsf"]

re_str = "^[_a-zA-Z]+[_a-zA-Z0-9]*$"

for name in name_list:

    # try:
    #     result = re.match(re_str, name).group()
    #     print(name, "合法")
    # except Exception as f:
    #     print(name + "不合法")
    result = re.match(re_str, name)
    if result:
        print(name, "合法")
    else:
        print(name, "不合法")