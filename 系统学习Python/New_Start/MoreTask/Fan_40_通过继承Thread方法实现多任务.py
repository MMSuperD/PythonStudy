# coding=utf-8
import threading
import time


class MyThread(threading.Thread):

    def run(self) -> None:  # 用类继承实现多任务这个方法是必须重写的
        print("run 方法被调用了", end="\n")
        self.demo()

    def demo(self):
        """测试多任务的函数"""
        for i in range(5):
            time.sleep(1)
            print("demo :  %d" % i)


def test():
    th1 = MyThread()  # 只会创建一个线程
    th1.start()

    print("测试函数")

    while True:
        th_nmber = len(threading.enumerate())
        print(threading.enumerate())  # 这个函数是打印有多少个线程正在运行
        time.sleep(0.5)
        if th_nmber <= 1:
            break


def main():
    test()


if __name__ == '__main__':
    main()
