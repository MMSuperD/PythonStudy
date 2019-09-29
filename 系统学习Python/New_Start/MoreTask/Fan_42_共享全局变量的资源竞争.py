import threading
import time

g_num = 0

# 创建互斥锁
metux = threading.Lock()


def test1(number):
    global g_num
    # 这个是第一种
    # metux.acquire()  # 上锁
    # for i in range(number):
    #     g_num += 1
    # metux.release()  # 解锁
    # 这个是第二种
    for i in range(number):
        metux.acquire()  # 上锁
        g_num += 1
        metux.release()  # 解锁
    print("g_num = " + str(g_num))


def test2(number):
    global g_num
    # metux.acquire()  # 上锁
    # for i in range(number):
    #     g_num += 1
    # metux.release()  # 解锁

    for i in range(number):
        metux.acquire()  # 上锁
        g_num += 1
        metux.release()  # 解锁
    print("g_num = " + str(g_num))


def main():

    th1 = threading.Thread(target=test1, args=(10000000,))
    th2 = threading.Thread(target=test2, args=(10000000,))

    th1.start()
    th2.start()

    time.sleep(2)

    print("g_num = " + str(g_num))




if __name__ == '__main__':
    main()