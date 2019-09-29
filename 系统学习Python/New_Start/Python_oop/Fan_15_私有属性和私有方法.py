
# 子类中不能够直接访问父类的属性和方法,要变为私有属性和方法,只要在前面加上__ 就可以了,子类可以直接访问父类的共有属性和方法

class A:

    def __init__(self):
        self.__name = "张三"
        self.sex = "man"
    pass


class B(A):
    pass


b = B()

print(b.sex)