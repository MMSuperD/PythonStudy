

class Money():
    """类的说明"""

    def __init__(self):
        self.__money = 100


    def setMoney(self, value):

        if isinstance(value, int):
            self.__money = value
        else:
            print("不符合要求")


    def getMoney(self):
        return self.__money


    money = property(getMoney, setMoney)


money = Money()

print(money.money)

money.money = 300

print(money.money)

