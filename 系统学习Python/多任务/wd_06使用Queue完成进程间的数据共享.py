import multiprocessing
import time

def download_data(q):
    """这里是模拟下载数据"""
    data_array = [12,"1223","jjfd"]

    for temp in data_array:
        q.put(temp)

    print("这里是下载数据完成")


def analyze_data(q):
    """这里是使用数据,也就是处理数据"""
    data_array = list()

    while True:
        if not q.empty():
            data_temp = q.get()
            data_array.append(data_temp)
        else:
            break

    print(data_array)
    print("这里是处理数据使用数据 %s",str(data_array))


def main():
    #创建一个Queue
    q = multiprocessing.Queue()  #如果设置Queue(3) 最多就只能有三个值,如果不设置,根据电脑里面的系统自己判断

    #创建两个进程
    p1 = multiprocessing.Process(target=download_data,args=(q,))
    p2 = multiprocessing.Process(target=analyze_data,args=(q,))

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()