# 自定义过滤器

# 过滤器 其实就是python函数

from django import template
from functools import singledispatch  # 这是是为了实现像C++ 中函数的重载 也就是相同函数名，不同的参数个数，或是不同参数类型
register = template.Library()

# 自定义过滤器 至少一个参数，最多两个参数
@register.filter
def mod(num,var=0):
    """判断num 是否为偶数"""
    if var == 0:
        return num%2 == 0;
    else:
        # 判断一个数是否是另一个数的倍数
        if num == 0 or var == 0:
            return False;
        return num % var == 0;
