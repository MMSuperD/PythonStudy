


#  生成器是特殊的迭代器

def create_num(number):
    """创建数字"""
    a, b = 0, 1
    current_number = 0

    while True:
        if current_number <= number:
            # print(a)
            yield a  # 如果函数中有yield 说明这个这个函数就不是函数了,而是一个生成器模板
            a, b = b, a + b
            current_number += 1
        else:
            break

    return "ok-----"


# 调用函数的时候,其实就是创建了一个生成器对象. 我们可以通过for循环进行迭代这个生成器对象,也可以用 next()方法调用这个迭代器,返回值
obj = create_num(10)

while True:

    try:
        print(next(obj))

    except Exception as result:
        print(result)
        print(result.value)
        break

