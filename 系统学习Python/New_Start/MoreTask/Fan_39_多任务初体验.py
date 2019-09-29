import threading  # 多任务模块
import time   # 睡眠模块

def test_funtion_1():
    """测试函数"""
    for i in range(5):
        print("test_functionn_1: %d" % i)
        time.sleep(1)

def test_demo():
    """测试函数"""
    th1 = threading.Thread(target=test_funtion_1)  # 这个是创建了一个对象
    th2 = threading.Thread(target=test_funtion_1)
    th1.start()  # 这个方法是创建线程
    th2.start()

    # 这里是确保while True 在 start() 后面运行
    time.sleep(1)

    # 打印线程的数量
    while True:
        lens = len(threading.enumerate())
        print(threading.enumerate())
        if lens <= 1:
            break;




def main():
    test_demo()

if __name__ == '__main__':
    main()