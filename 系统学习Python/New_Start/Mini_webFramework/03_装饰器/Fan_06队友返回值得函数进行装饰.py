def vaild_test2(func):
    print("--------开始装饰---------")
    def create_test(*args, **kwargs):
        print("----------权限认证 1-----------")
        print("----------权限认证 2-----------")
        return func(*args,  **kwargs)  # 这里的*   ** 是拆包的意思
    return create_test

@vaild_test2   # 等价于 test1 = vaild_test2(test1) 所谓的装饰器 就相当于一个语法糖 一个代码块
def test1(a, *args, **kwargs):
    print("----------test1------- %d" % a)
    print("----------test1-------" , args)
    print("----------test1-------" , kwargs)
    print("*" * 100)
    return "ok"



test1(100)
test1(100,2000,2322,232)
test1(100, 2332, 'dsfsdf', m=23)

print("-------end------- %s" % test1(100, 232, 232, "3232", m=44))
