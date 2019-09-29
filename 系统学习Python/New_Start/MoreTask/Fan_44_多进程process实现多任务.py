import multiprocessing
import time

def test1():
    for i in range(5):
        time.sleep(1)
        print("test1:" + str(i))


def test2():
    for i in range(5):
        time.sleep(1)
        print("test2:" + str(i))


def main():
    process1 = multiprocessing.Process(target=test1)  # 创建一个进程
    process2 = multiprocessing.Process(target=test2)

    process1.start()
    process2.start()


if __name__ == '__main__':
    main()