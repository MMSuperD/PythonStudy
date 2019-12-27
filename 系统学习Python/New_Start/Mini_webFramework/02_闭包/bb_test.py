
x = 300

def test():
    x = 200
    def test2():
        nonlocal x
        print("x =  %d" % x)
        x = 100
        print("x =  %d" % x)

    print("x = %d" % x)
    return test2


t1 = test()
t1()


