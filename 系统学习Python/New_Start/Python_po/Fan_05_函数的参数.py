def sum_2_num():
    """对两个数字求和"""
    num1 = 1
    num2 = 3

    print("%d + %d = %d" % (num1, num2, num1 + num2))


sum_2_num()


def sum_num(num1, num2):
    """对两个数字求和"""
    print("%d + %d = %d" % (num1, num2, num1 + num2))

    return num2 + num1


hh = sum_num(10, 20)

print(hh)


# 函数的嵌套调用


def test1():
    print("test1")


def test2(num):
    """文档注释

    :param num:
    """
    test1()
    print("test2 + %d" % num)


test2(2)


def demo(num, num2, nun3):
    """

    :param num:
    :param num2:
    :param nun3:
    """
    print("hello")

demo(1,2,3)