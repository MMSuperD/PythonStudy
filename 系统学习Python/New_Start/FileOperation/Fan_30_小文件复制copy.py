
# 1.打开文件
read_file = open("hello.txt", "r")   # 只读
write_file = open("hello[副本].txt", "a")  # 追加


# 2.只读文件打开  追加文件打开副本

while True:
    read_text = read_file.readline()
    if not read_text:
        break
    write_file.write(read_text)

# 3.关闭文件
read_file.close()
write_file.close()