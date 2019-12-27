

def application(dict, set_response_header):
    """功能函数接口"""
    set_response_header("200 OK", [("Content-Type", "text/plain; charset=utf-8"), ("Server", "Fan 1.1")])

    print(dict["source_path"])
    return "hello python! %s" % fun_select(dict)


def fun_select(dic):
    """功能选择页面"""
    source_path = dic["source_path"]
    if source_path == "register":
        return register()
    elif source_path == "login":
        return login()
    elif source_path == "forget_password":
        return forget_password()
    elif source_path == "auth_code":
        return auth_code()
    else:
        return "没有响应的页面"

def register():
    """注册页面"""
    return "register page(注册页面)"

def login():
    """登录页面"""
    return "login page(登录页面)"

def forget_password():
    """忘记密码页面"""
    return "register page(忘记密码页面)"

def auth_code():
    """短信验证页面"""
    return "auth_code page(短信验证页面)"


