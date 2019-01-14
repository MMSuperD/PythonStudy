
from collections.abc import Iterable
from collections.abc import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为 可以迭代的对象 ,及可以使用 for ,那么必须实现 __iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            temp = self.names[self.current_num]
            self.current_num += 1
            return temp
        else:
            raise StopIteration  #这个是停止for循环 抛出异常,就停止了




classmate = Classmate()
classmate.add("zhang san")
classmate.add("li shi")
classmate.add("wang wu")

print("判断classmate 是否是可以迭代的对象:",isinstance(classmate,Iterable))

classmate_iterator = iter(classmate)

print("判断classmate_iterator 是否是迭代器",isinstance(classmate_iterator,Iterator))

for temp in classmate:
    print(temp)
    time.sleep(1)

