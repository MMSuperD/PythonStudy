
temp = True
while temp:
    try:
        # 不能够正常执行的代码
        num = int(input("请输入整数:"))
        temp = False
    except:
        print("请输入正常的整数:", end="")




print("_" * 50)