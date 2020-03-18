
from django.http import HttpResponse
#　from django.utils.deprecation import MiddlewareMixin
import sys
import inspect



# 中间类的作用方便与在多个地方添加装饰器,也可以用于拦截

class BlockIPSMiddleware:
    """中间类"""
    def __init__(self, get_response):
        """服务器重启之后,接受到的第一个请求,会调用这个init方法"""
        self.get_response = get_response
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber,funcName)
        ｐrint(1);

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber, funcName)

        return response


    def process_view(self,request,view_func,*view_args,**view_kwargs):
        """视图函数调用前会调用"""
        # 这个是要拒绝的ip地址list
        REFUSE_IPS = ['192.168.1.23'];

        # 获取访问的ip
        user_ip = request.META["REMOTE_ADDR"];

        if user_ip in REFUSE_IPS:
            return HttpResponse("你的ip被我们禁止了");


    def process_exception(self, request, exception):

        return HttpResponse(exception)



class Test11Middleware:
    """测试中间件函数的调用顺序"""

    def __init__(self, get_response):
        """服务器重启之后,接受到的第一个请求,会调用这个init方法"""
        self.get_response = get_response
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber,funcName)
        print(2)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber, funcName)

        return response


    def process_view(self,request, view_func, view_args, view_kwargs):
        """process_view() 只在 Django 调用视图前被调用"""

        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber, funcName)

    def process_exception(self, request, exception):
        """视图异常的时候会被调用"""
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber, funcName)

        #return HttpResponse('server bad');


    def process_template_response(self, request, response):
        """这个是视图函数调用完之后在调用"""
        '''
        执行 process_template_response 函数有一个前提条件，
        那就是视图函数返回的对象要有一个 render() 方法
        （或者表明该对象是一个 TemplateResponse 对象或等价方法
        '''
        funcName = sys._getframe().f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
        print(lineNumber, funcName)
        return response;

