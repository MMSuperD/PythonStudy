

class Tool(object):
    """类的描述"""

    def get_bar(self):
        print("get_bar")
        return "get_bar"


    def set_bar(self, value):
        """必须有有且只有两个参数"""
        print("set_bar")
        return "set_bar"


    def del_bar(self):
        print("del_bar")
        return "del_bar"


    BAR = property(get_bar, set_bar, del_bar, "描述信息")


tool = Tool()

print(tool.BAR)  # 自动调用property 属性中的第一个参数中的方法

tool.BAR = "2323"  # 自动调用property 属性中的第二个参数中的方法

print(tool.BAR)  # 自动调用property 属性中的第一个参数中的方法

print(Tool.BAR.__doc__)  # 自动调用property 属性中的第四个参数中的方法

del tool.BAR  # 自动调用property 属性中的第三个参数中的方法