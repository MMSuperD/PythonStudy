info_tuple = ("dfsd",)  # 只有一个元素的元组必须后面有一个逗号

# 取值
print(info_tuple[0])

# 元组的遍历
infos_tuple = ("dsfs",12,"sdfsds","ghjk")

for my_info in infos_tuple:

    print(str(my_info) + " hello")


# 格式化字符串

detail_tuple = ("小明",12,13.5)

print("%s %d %.2f" % detail_tuple)

detail_str = "%s %d %.2f" % detail_tuple

print(detail_str)