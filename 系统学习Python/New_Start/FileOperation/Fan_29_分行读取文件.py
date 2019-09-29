
# 打开文件
file = open("hello.txt","r")

# 读取文件
while True:
    text = file.readline()  # readline() 这个函数一行一行的读取数据 ,读取一行移动一行数据
    if not text:  # 这个是判断是否读取到内容
        break
    print(text,end="")

# 关闭文件
file.close()