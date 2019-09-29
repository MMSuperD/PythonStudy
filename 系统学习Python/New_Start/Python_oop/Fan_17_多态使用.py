
class Dog:

    def __init__(self, name):
        self.name = name

    def game(self):

        print("%s 正在学习飞" % self.name)


class  XiaoTianQuan(Dog):

    def game(self):

        print("哮天犬在飞")


dog = Dog("nn")

dog.game()

xtq = XiaoTianQuan("哮天犬")

xtq.game()