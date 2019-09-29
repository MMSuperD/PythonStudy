from collections.abc import Iterable  # 可迭代对象
from collections.abc import Iterator  # 迭代器


class Classmate():
    """迭代器的初次使用类"""

    def __init__(self):
        self.names = list()
        self.current = 0

    def __iter__(self):
        """只要存在这个方法就证明这个类创建出来的对象是一个可以迭代的对象"""
        return self

    def __next__(self):
        """只要同时存在__iter__ 和 __next__方法就证明这个类创建出来的对象是一个迭代器"""
        if self.current < len(self.names):
            temp = self.current
            self.current = self.current + 1
            return self.names[temp]
        else:
            raise StopIteration  # 这个返回异常是为了停止迭代

    def add_classmate(self, name):
        """添加铜须姓名"""
        self.names.append(name)


def main():
    # 1.创建一个可以迭代的对象
    classmate = Classmate()
    classmate.add_classmate("王五")
    classmate.add_classmate("历史")
    classmate.add_classmate("张三")

    # 2.判断一个对象是否是可以迭代的对象

    print("该对想是否是一个可以迭代的对象:", isinstance(classmate, Iterable))
    print("该对想是否是一个迭代器:", isinstance(classmate, Iterator))

    for name in classmate:
        print(name)


if __name__ == '__main__':
    main()
