import threading
import time


def test1(num_list):
    time.sleep(1)
    global num
    num += 100
    print("num: %d" % num)

    num_list.append("hello")
    print(num_list)


def test2():
    time.sleep(1)

    print("num: %d" % num)
    print(num_list)



num = 1  # 这是一个全局变量

num_list = [12,32,232,"ghj"]

def main():
    th1 = threading.Thread(target=test1,args=(num_list,))  # 可以穿参数 args
    th2 = threading.Thread(target=test2)
    th1.start()
    time.sleep(1)  # 这是是为了保证test() 函数先执行完
    th2.start()

    print("num: %d" % num)
    print(num_list)


if __name__ == '__main__':
    main()
