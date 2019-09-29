
class Cat:

    def __init__(self,name="Fan", age=26):

        self.name = name
        self.age = age

    def __del__(self):

        print("我 去 了")

    def __str__(self):

        return " %s 今年 %d 岁了" % (self.name, self.age)


cat = Cat()

print(" %s 今年 %d 岁了" % (cat.name,cat.age))

print(cat)

