

def set_lever(lever_num):
    def vaild_test(func):
        def vaild_call(*args, **kwargs):
            print("-------权限认证------")

            if lever_num == 1:
                print("-------权限1验证-------")
            elif lever_num == 2:
                print("-------权限2认证-------")
            else:
                print("------普通权限认证-------")
            return func()
        return vaild_call
    return vaild_test

@set_lever(3)
@set_lever(2)
@set_lever(1)   # 带有参数的装饰器 执行顺序是,先调用函数,函数的返回值作为装饰器装饰
def test():
    return "Hello world"

test()