import time


def task_1():
    while True:
        time.sleep(0.1)
        print("-----------1-------")
        yield


def task_2():
    while True:
        time.sleep(0.1)
        print("-----------2-------")
        yield


def main():
    t1 = task_1()
    t2 = task_2()

    while True:
        next(t1)
        next(t2)



if __name__ == '__main__':
    main()