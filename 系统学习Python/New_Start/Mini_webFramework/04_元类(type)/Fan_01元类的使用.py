

# 通过type  创建 class

@classmethod
def class_method_test(cls):
    print("class_method_test",cls)
    pass

@staticmethod
def static_method_test():
    print("static_method_test")
    pass


class_test = type("Class_Test", (object, ),{"class_method_test":class_method_test, "static_method_test":static_method_test, "a":100, "b":{"m":"hello world"}})

cls = class_test()

cls.class_method_test()
cls.static_method_test()
print(cls.a)
print(cls.b)