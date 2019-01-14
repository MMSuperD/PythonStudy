
import threading
import time

number = 100

list_array = ["100","200"]

def test1(num):
    global number
    for i in  range(num):
        number += i

    print("______test1______ %d" % number)


def test2(num):
    global number
    for i in range(num):
        number += i

    print("______test2______ %d" % number)

def test3(list_array):
    print("list_array: %s", str(list_array))

def test4(list_array):
    list_array.append("300")
    print("list_array: %s",str(list_array))



def main():
    #这个是打印当前正在运行的线程
    print(threading.enumerate())
    print("current number: %d" % number)

    t1 = threading.Thread(target=test1,args=(1000,))
    t2 = threading.Thread(target=test2,args=(1000,))

    t3 = threading.Thread(target=test3,args=(list_array,))
    t4 = threading.Thread(target=test4,args=(list_array,))
    t1.start()
    t2.start()

    t4.start()
    t3.start()

    print("end number: %d" % number)

    print("list_array: %s", str(list_array))

if __name__ == '__main__':
    main()