
def demo():
    return int(input("亲输入整数:"))

def demo2():
    return demo()

def demo3():
    return demo2()


try:
    print(demo3())
except Exception as result:
    print("未知的错误: %s" % result)
