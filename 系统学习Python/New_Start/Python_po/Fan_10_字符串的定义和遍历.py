hh_str = "ghjkgbhjkghjk"

i = 0
for st in hh_str:
    print(st)
    i = i + 1
    print(i)


hello_str = "hello hello"
# 统计字符串的长度
print(len(hello_str))

# 统计某一个小字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))  # 这句话会报错应为不存在这个字符串

# 某一个字符串出现的位置

print(hello_str.index("llo"))  # 找到第一个字符串之后就返回了如果找不到也就报错了