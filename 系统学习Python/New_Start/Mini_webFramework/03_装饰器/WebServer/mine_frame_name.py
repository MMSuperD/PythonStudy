
# 这个是通过装饰器实现路由的功能
FUNC_DICT = dict()

def set_key(path_key):
    def create_dec(func):
        #  这句话的作用就是 把路径当做key  把 功能函数的引用当做值
        FUNC_DICT[path_key] = func
        def create_call(*args, **kwargs):
            return func()
        return create_call
    return create_dec


def fun_select(dic):
    """功能选择页面"""
    source_path = dic["source_path"]
    try:
        return FUNC_DICT[source_path]()
    except Exception as ret:
        print("没有找到响应的界面")
        return "没有找到相应的页面"

@set_key("register")
def register():
    """注册页面"""
    return "register page(注册页面)"

@set_key("login")
def login():
    """登录页面"""
    return "login page(登录页面)"

@set_key("forget_password")
def forget_password():
    """忘记密码页面"""
    return "register page(忘记密码页面)"

@set_key("auth_code")
def auth_code():
    """短信验证页面"""
    return "auth_code page(短信验证页面)"

def application(dict, set_response_header):
    """功能函数接口"""
    set_response_header("200 OK", [("Content-Type", "text/plain; charset=utf-8"), ("Server", "Fan 1.1")])

    print(dict["source_path"])
    return "hello python! %s" % fun_select(dict)



