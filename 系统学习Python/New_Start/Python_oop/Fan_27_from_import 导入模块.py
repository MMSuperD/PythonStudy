

# 语法 from  模块名字  import 导入的工具  as  工具别名

# from 模块名字 import * 可以导入这个模块的所有的工具,开发中少用.不推荐使用

# 如果从两个不同的模块中导入相同的工具,后导入的会覆盖前一个导入的模块

#from Fan_16_多继承使用 import C as MM

from Python_oop import Fan_16_多继承使用

c = Fan_16_多继承使用.C()

print(c)

print(Fan_16_多继承使用.__file__)  # 查看导入模块的路径


#  为了让我们开发的模块能够被他人使用我们需要使用__name__ 这个内置的属性,写测试代码

def main():
    print("测试代码")


if __name__ == "__main__":
    main()


