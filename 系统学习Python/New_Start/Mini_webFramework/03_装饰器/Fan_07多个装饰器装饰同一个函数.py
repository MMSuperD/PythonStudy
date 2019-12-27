
#  多个装饰器装饰同一个函数 装饰执行:提交从上到下执行  装饰顺序: 从下往上执行
def vaild_test1(func):
    print("--------开始装饰1---------")
    def create_test(*args, **kwargs):
        print("----------权限认证 1-----------")
        func(*args,  **kwargs)  # 这里的*   ** 是拆包的意思
    return create_test

def vaild_test2(func):
    print("--------开始装饰2---------")
    def create_test(*args, **kwargs):
        print("----------权限认证 2-----------")
        func(*args,  **kwargs)  # 这里的*   ** 是拆包的意思
    return create_test

@vaild_test1
@vaild_test2   # 等价于 test1 = vaild_test2(test1) 所谓的装饰器 就相当于一个语法糖 一个代码块
def test(a, *args, **kwargs):
    print("----------test1------- %d" % a)
    print("----------test1-------" , args)
    print("----------test1-------" , kwargs)
    print("*" * 100)

test(100)
test(100,2000,2322,232)
test(100, 2332, 'dsfsdf', m=23)