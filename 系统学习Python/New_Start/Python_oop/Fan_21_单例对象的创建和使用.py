class MusicPlayer:

    # 保存第一次创建的对象
    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):

        # 1.创建对象的时候,系统会自动调用
        print("创建了一个新的对象")

        # 2.为对象分配空间

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 3.返回对象的引用
        return cls.instance



player = MusicPlayer("小明")

player2 = MusicPlayer("小明")
print(player)
print(player2)