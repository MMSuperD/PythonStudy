import os
import multiprocessing


def copy_file(file_name, new_folder_name, old_folder_name, queue):
    """copy 文件功能"""
    #print("文件:%s 从:%s文件夹中 拷贝到:%s中" %(file_name, old_folder_name, new_folder_name))

    # 1.读取文件内容
    old_file = open("./" + old_folder_name + "/" + file_name, "rb")
    file_content = old_file.read()
    old_file.close()

    # 2.创建文件写内容
    new_file = open("./" + new_folder_name + "/" + file_name, "wb")
    new_file.write(file_content)
    new_file.close()

    queue.put(file_name)

def main():
    # 1.获取用户需要copy 的文件夹的名字啊
    old_folder_name = input("请输入要copy 的文件夹名字:")

    # 2.创建新的文件夹
    try:
        new_folder_name = old_folder_name + "[复本]"
        os.mkdir("./" + new_folder_name)
    except:

        pass

    # 3.获取要copy 的文件.

    file_names = os.listdir(old_folder_name)
    #print(file_names)

    # 4.创建进程池
    pools = multiprocessing.Pool(5)

    # 4.1创建队列用来通信获取copy进度
    queue = multiprocessing.Manager().Queue()

    # 5.向进程池中添加任务
    for file_name in file_names:
        pools.apply_async(copy_file,args=(file_name, new_folder_name, old_folder_name, queue))

    # 6.关闭进程池池
    pools.close()
    #pools.join()  # 等待子进程池的关闭

    sum = 0
    while True:

        file_name = queue.get()

        #print("%s 文件拷贝完成" % file_name)
        sum = sum + 1
        hh = sum / int(len(file_names)) * 100
        print("%.2f" % hh)
        if sum == len(file_names):
            break

    print("----------文件拷贝结束----------")


if __name__ == '__main__':
    main()
