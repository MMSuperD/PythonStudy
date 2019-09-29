class Cat:

    def eat(self):
        """吃东西"""
        print("eat")

    def drink(self):
        """喝东西"""
        print("drink")



cat = Cat()

cat.eat()

print(cat)
print("%d" % id(cat))