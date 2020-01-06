

class Good(object):
    """货物类"""

    def __init__(self):
        """对象的初始化"""
        # 原价
        self.origin_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        """实际价格"""
        return self.origin_price * self.discount

    @price.setter
    def price(self, value):
        """设置原价"""
        self.origin_price = value


    @price.deleter
    def price(self):
        """删除这个属性"""
        del self.origin_price


good = Good()

print(good.price)

good.price = 200

print(good.price)

del good.price

# 这句话会报错
print(good.price)


