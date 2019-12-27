def vaild_test2(func):
    print("--------开始装饰---------")
    def create_test():
        print("----------权限认证 1-----------")
        print("----------权限认证 2-----------")
        func()
    return create_test

@vaild_test2   # 等价于 test1 = vaild_test2(test1) 所谓的装饰器 就相当于一个语法糖 一个代码块
def test1():
    print("----------test1-------")