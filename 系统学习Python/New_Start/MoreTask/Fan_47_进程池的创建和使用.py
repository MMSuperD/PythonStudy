from multiprocessing import Pool
import os, time, random

def work_async(number):
    """异步代码"""
    time_start = time.time()
    time.sleep(random.random() * 2)
    # 这里的打印数据是不能显示出来的
    print("进程号为:%d 数据 : %s" % (os.getegid(), str(number)))  # 进程号
    time_end = time.time()
    print("使用时间:%f" % (time_end - time_start))


def main():
    # 创建进程池
    pools = Pool(3)  # 表示池子里面最多有三个进程, 如果不写数量,就根据系统的能力

    # 添加任务
    for i in range(10):

        pools.apply_async(work_async, (i, ))

    print("---------开始---------")
    pools.close()  #关闭进程池
    pools.join()  #必须加上这句话,等所有的子进程结束后才会有结束主进程
    print("---------关闭---------")


if __name__ == '__main__':
    main()