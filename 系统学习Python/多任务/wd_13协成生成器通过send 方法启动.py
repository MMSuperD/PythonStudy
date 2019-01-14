
def create_num(all_num):
    print("--------1--------")
    #a = 0
    #b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("-------2-------")
        #print(a)
        ret = yield(a)  #如果一个函数中有yield 语句,那么这个就不是函数,而是一个生成器模板
        print(">>>>>>>>",ret)
        print("-------3-------")
        a, b = b, a + b
        current_num += 1
        print("-------4---------")

    return "ok"


#如果在调用create_num 的时候,发现这个函数中有yield  这个关键字,不是调用函数,而是创建一个生成器模板对象

#生成器也是特殊的迭代器



obj = create_num(2)   #如果调用next 方法次数多余2 就会越界,异常所以我们需要处理这个异常

ret = obj.send("hhhhhhh")  #send 方法里面的参数就是  yeild a 的值  send 方法最好不要用第一次启动生成器 如果一定要启动生成器, send(None),因为那个时候没有可以接参数的值


