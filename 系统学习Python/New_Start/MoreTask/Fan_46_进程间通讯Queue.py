import multiprocessing


def download_data(q):
    data_list = ["hello", "mmd", 12, 343]
    for temp in data_list:
        q.put(temp)

    print("数据下载完成----------------")


def analyze_data(q):
    """分析数据"""
    analyze_data_list = list()

    # 从队列中获取数据
    while True:
        data = q.get()
        analyze_data_list.append(data)

        if q.empty():
            break

    # 数据处理完成
    print(analyze_data_list)



def main():
    # 创建一个队列
    q = multiprocessing.Queue()  # Queue(3)表示最多三个元素 ,如果不填3 根据系统资源来判断

    th1 = multiprocessing.Process(target=download_data, args=(q,))
    th2 = multiprocessing.Process(target=analyze_data, args=(q,))

    th1.start()
    th2.start()

if __name__ == '__main__':
    main()