
# 字典里面得键值对是无序的 键肯定是惟一的 只能是str,list,tuple 三种类型 一般使用 str
xiaoming = {"name":"xiaoming",
            "age":12,
            "weight":180}

print(xiaoming)

# 取值
print(xiaoming["name"])

# 增加/修改
xiaoming["favarite"] = "love"  # 增加 不存在的键值对 添加
xiaoming["name"] = "小小明"  # 修改 有的话修改



# 删除

xiaoming.pop("name")
print(xiaoming)

# 是否存在否一个键值对


# 统计键值对的数量

print(len(xiaoming))

# 合并字典
# update 方法


# 遍历字典

for key in xiaoming:
    print("%s - %s" % (key,xiaoming[key]))