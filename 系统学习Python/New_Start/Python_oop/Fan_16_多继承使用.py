

# 多继承使用,如果存在父类中存在同名的属性和方法


class A:

    def demo(self):
        print("A")
    pass


class B:
    def demo(self):
        print("B")
    pass


class C(A,B):
    pass


c = C()

c.demo()

#  __mro__ 内置属性 查找方法调用的顺序

print(C.__mro__)  #按照这个输出顺序来执行的