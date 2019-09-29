
# 1.打开文件
file = open("./hello.txt")

# 2.read or write file
content = file.read()  # 文件指针第一次从开始位置开始,如果读完了,第二次的就会直接在文件末尾
print(content)

# 3.关闭文件
file.close()

