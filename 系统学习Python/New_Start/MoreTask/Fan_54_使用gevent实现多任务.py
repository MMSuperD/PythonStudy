import gevent
from gevent import monkey
import time

monkey.patch_all()  # 这个是打补丁 如果没有这个,所有的time 都需要编程 gevent.sleep()


def task_1(n):
    for i in range(n):
        time.sleep(0.1)
        print("-----------%d-------" % i)


def task_2(n):
    for i in range(n):
        time.sleep(0.1)
        print("-----------%d-------" % i)


def task_3(n):
    for i in range(n):
        time.sleep(0.1)
        print("-----------%d-------" % i)



def main():

    print("start")

    g1 = gevent.spawn(task_1, 5)
    g2 = gevent.spawn(task_1, 5)
    g3 = gevent.spawn(task_1, 5)

    g1.join()
    g2.join()
    g3.join()

    # 简洁方式实现多任务
    # gevent.joinall([
    #     gevent.spawn(task_1, 5),
    #     gevent.spawn(task_2, 5),
    #     gevent.spawn(task_3, 5)
    # ])

    print("end")

if __name__ == '__main__':
    main()