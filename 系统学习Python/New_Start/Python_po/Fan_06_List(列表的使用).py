name_list = ["I","He","She"]

print(name_list)
print(name_list[-3])

# 取值
print(name_list[0])

# 根据值去的索引,如果传递的数据不再列表中,程序会报错
print(name_list.index("He"))


# 修改指定位置的数据
name_list[1] = "We"
print(name_list)

# 列表中增加数据
name_list.append("him")
print(name_list)
name_list.insert(0,"her")  # 指定位置插入元素
print(name_list)
name_list.extend(["its","himself","him"])
print(name_list)

# 删除数据

del name_list[1]  # 关键之把一个变量从内存中删除
print(name_list)

name_list.remove("himself")
print(name_list)
print(name_list.pop())  #默认删除最后一个元素
print(name_list)
# name_list.clear()  # 清空列表
print(name_list)


# 列表的长度
list_len = len(name_list)
print(list_len)


# 列表的排序

print(name_list.sort())
print(name_list)
name_list.sort(reverse=True)
print(name_list)

# 列表反转
name_list.reverse()
print(name_list)


# 列表的循环遍历

for name in  name_list:
    print(name)