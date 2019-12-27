

# 通过魔法方法给类添加属性

def add_type_property(class_name, class_object, class_property):
    attrbutie = dict()
    for key, value in class_property.items():
        attrbutie[key]=value
    attrbutie["name"]="王丹"
    return type(class_name, class_object, attrbutie)


class BaseType(object, metaclass=add_type_property):
    a = 100
    pass


cls = BaseType()
BaseType.mm = 200  # 这个是给类添加属性
print(BaseType.mm)
print(cls.name)