
import os
import multiprocessing

def copy_file(q,file_name,new_floder_name,old_floder_name):
    """完成文件的复制"""
    # print("======模拟copy 文件由老的文件:%s 拷贝到新的文件夹: %s 文件的名字是 %s" % (old_floder_name,new_floder_name,file_name))
    #1.打开老的文件
    old_file = open(old_floder_name + "/" + file_name,"rb")
    #2.读取内容
    content = old_file.read()
    old_file.close()

    #3.创建新的文件
    new_file = open(new_floder_name + "/" + file_name,"wb")
    new_file.write(content)
    new_file.close()

    #4.拷贝一个文件结束,我们需要向queue 中添加一个项目完成
    q.put(file_name)

def main():
    """主函数"""
    #1.获取用户要copy的文件夹名字
    old_floder_name = input("请输入要copy 的文件夹名字:")

    #2.创建文件夹副本,这里保证只创建一次文件夹
    try:
        new_floder_name = old_floder_name + "[复件]"
        os.mkdir(new_floder_name)
    except:
        pass
    #3.获取文件夹类所有的名字 listdir()
    file_names = os.listdir(old_floder_name)

    #4.创建进程池用来控制进程的数量
    po = multiprocessing.Pool(5)

    #4.1 创建Queue  用来做进程间通讯
    q = multiprocessing.Manager().Queue()

    #5.向进程池中添加任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,new_floder_name,old_floder_name,))

    #6.停止进程等待做完
    po.close()
   # po.join(),我们可以再主进程中做展示进度,读取queue

    file_all_count = len(file_names)
    finish_count = 0
    while True:
        #获取文件名字
        file_name = q.get()
        finish_count += 1
        print(" \r 完成拷贝的文件名字:%s progress:%.2f %%" % (file_name,(finish_count * 100 / file_all_count)),end="")  #,end="" 表示不换行 
        if finish_count >= file_all_count:
            print("end copy")
            break




if __name__ == '__main__':
    main()