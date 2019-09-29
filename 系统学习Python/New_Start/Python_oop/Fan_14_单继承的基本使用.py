class Animal:
    """动物的基类"""

    def eat(self):
        """吃"""
        print("吃")

    def drink(self):
        """喝"""
        print("喝")

    def run(self):
        """跑"""
        print("跑")

    def sleep(self):
        """睡"""
        print("睡")


class Dog(Animal):
    """狗"""

    def call(self):
        """叫"""
        print("叫")

    def sleep(self):
        """睡的更认真 重写父类中中的方法"""
        super(Dog, self).sleep()  # 调用父类的方法
        print("睡的更认真")


dog = Dog()

dog.sleep()
dog.call()
