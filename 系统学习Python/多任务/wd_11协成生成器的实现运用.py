
def create_num(all_num):
    print("--------1--------")
    #a = 0
    #b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("-------2-------")
        #print(a)
        yield(a)  #如果一个函数中有yield 语句,那么这个就不是函数,而是一个生成器模板
        print("-------3-------")
        a, b = b, a + b
        current_num += 1
        print("-------4---------")


#如果在调用create_num 的时候,发现这个函数中有yield  这个关键字,不是调用函数,而是创建一个生成器模板对象

#生成器也是特殊的迭代器



obj = create_num(10)

ret = next(obj)  #只要是迭代器就可以调用next 方法
print(ret)

for num in obj:
    print(num)