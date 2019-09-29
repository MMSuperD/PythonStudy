
class Cat:

    def __init__(self,name="Fan", age=26):

        self.name = name
        self.__age = age  # 加上__ 就变成了私有属性了

    def __del__(self):

        print("我 去 了")

    def __str__(self):

        #self.__create()

        return " %s 今年 %d 岁了" % (self.name, self.__age)

    def __create(self):

        print("mmd")





cat = Cat()

#cat.__create()  #__开始就变成私有方法了
print(cat)

# 私有属性 和 私有方法特殊访问方法 ,一般情况下不要使用

print(cat._Cat__create())

