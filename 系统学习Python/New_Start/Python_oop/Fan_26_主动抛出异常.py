
def input_password():

    password = input("请输入长度大于八 的密码:")

    if len(password) >= 8:
        return  password

    print("抛出密码不符合要求的异常")

    # 1.定义异常对象,这里的描述信息可以作为参数传递
    ex = Exception("密码长度不符合要求")

    # 2.抛出异常
    raise ex

# 这里是捕获异常的代码
try:
    print(input_password())
except Exception as result:
    print(result)