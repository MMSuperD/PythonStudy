
# 异常处理是为了保证我们程序在运行的时候不能够奔溃,这样让用户体验超级差,如有有已知的错误一定要提前写,还没有未知错误都需要书写

try:
    num = int(input("请输入整数"))

    end = 8 / num

    print("结果是: %s" % str(end))

except ValueError:  # 这个是已知错误
    print("值得错误")
except Exception as result:  # 这里的result 自己定义的一个变量用来接收错误
    print("未知错误: %s" % result)

else:
    print("只有没有异常,才会执行else 代码")

finally:
    print("无论是否有异常都会执行finally 代码")