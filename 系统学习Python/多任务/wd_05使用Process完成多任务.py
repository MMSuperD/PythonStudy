import multiprocessing
import time

def test1():
    while True:
        print("processing ------1------")
        time.sleep(1)



def test2():
    while True:
        print("processing ------2------")
        time.sleep(1)



def main():

    #创建进程代码
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    #开始进程
    p1.start()
    p2.start()

    print("end")



if __name__ == '__main__':
    main()