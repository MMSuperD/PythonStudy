
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("实例对象加上() 就会调换用该方法")
        print("在这里,我们可以添加多个权限 😸")
        return self.func()


@Test  # 相当于 get_str = Test(get_str)
# @Test.静态方法  # 相当于 get_str = Test(get_str)
def get_str():
    return "Hello world"

print(get_str())

