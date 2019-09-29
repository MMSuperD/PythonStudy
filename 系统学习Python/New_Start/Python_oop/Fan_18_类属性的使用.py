
class Tools:
    """工具"""

    count = 0  # 这个是一个类属性

    def __init__(self, name):
        self.name = name

        Tools.count += 1

    @classmethod   #  这个是类方法的关键字
    def show_tools_count(cls):
        print("数量 %s" % Tools.count)


tools = Tools("榔头")
tools2 = Tools("斧头")

print(Tools.count)

#  也可以用对象名调用

print(tools.count)  # 查询机制 先在对象中查询 之后再去查询 类里面得知道查询到为止

Tools.show_tools_count()

