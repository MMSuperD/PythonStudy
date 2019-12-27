
# 装饰器的原理 就是交换方法 通过指针实现的饿
# 装饰器实现的原理
def vaild_test2(func):
    def create_test():
        print("----------权限认证 1-----------")
        print("----------权限认证 2-----------")
        func()
    return create_test

@vaild_test2   # 等价于 test1 = vaild_test2(test1) 所谓的装饰器 就相当于一个语法糖 一个代码块
def test1():
    print("----------test1-------")


# test1 = vaild_test2(test1)  # test1 指向  create_test 函数   func 指向 定义的test1方法
test1()