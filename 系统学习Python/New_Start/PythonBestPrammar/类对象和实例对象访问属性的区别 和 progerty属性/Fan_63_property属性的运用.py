

class Tool(object):
    """描述信息"""

    @property   # 相当于IOS 中的计算型属性,get 方法
    def size(self):
        return 100

tool = Tool()

# size = tool.size()  这样写是不对的,不能够传递参数,所以定义的时候也就只能有 self  了
size = tool.size

print(tool.size)