class MusicPlayer:


    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):

        # 1.创建对象的时候,系统会自动调用
        print("创建了一个新的对象")

        # 2.为对象分配空间

        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance



player = MusicPlayer("小明")

print(player.name)