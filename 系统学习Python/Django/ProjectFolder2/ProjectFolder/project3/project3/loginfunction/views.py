from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect

from loginfunction.models import UserInfo
from loginfunction.publicLibrary import public_pac

from django.conf import settings
from loginfunction.models import TestPic
from loginfunction.models import AreaData

import sys


# Create your views here.

def login(request):
    """这里是登录视图响应方法"""

    if request.session.has_key('isLogin'):  # 如果存在就返回首页
        return HttpResponseRedirect('/index');
    else:
        username = request.COOKIES.get("username");
        if username:
            return render(request, 'loginfunction/login.html', {"username": username})
    return render(request, 'loginfunction/login.html');


def ajax_login(request):
    """这个是 ajax 请求登录"""
    # 1.获取请求的参数据
    if request.method == 'GET':
        username = request.GET.get('username');
        password = request.GET.get('password');
        checkbox_select = request.GET.get('checkbox_select');
    elif request.method == 'POST':
        username = request.POST.get('username');
        password = request.POST.get('password');
        checkbox_select = request.POST.get('checkbox_select');
    else:
        username = None;

    # request.GET/POST  返回的数据是 QueryDict 类型
    # from django.http.request import QueryDict

    print('hello');
    # 2.数据库数据校验，是否对
    temp = UserInfo.objects.filter(username=username);
    if temp:
        if temp[0].password == password:
            # 校验成功之后需要存储记住账号
            response = JsonResponse({'res': 1});
            if checkbox_select == 'on':  # 这个表示要记住账号，只有登录成功的时候才需要记录账号
                response.set_cookie('username', username);
            # 登录成功之后我们需要保存登录状态，我们需要用session 来保存登录状态
            request.session["isLogin"] = 1;
            return response;  # 这个用户校验成功
        else:
            return JsonResponse({'res': 0});  # 这是个用户密码错误
    else:
        return JsonResponse({'res': 2});  # 这个是用户不存在


def index(request):
    funcName = sys._getframe().f_code.co_name  # 获取调用函数名
    lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
    print(lineNumber, funcName)
    return render(request, 'loginfunction/index.html');


def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie信息");
    # cookie 的键为：num 值为1
    response.set_cookie('num', 1);
    return response;


def get_cookie(request):
    """获取cookie值"""
    # 取出cookie信息
    cookie_value = request.COOKIES["num"];
    return HttpResponse(cookie_value);


def set_session(request):
    """设置session 的值"""
    request.session['username'] = 'fan';
    request.session['age'] = 18;
    return HttpResponse("设置session信息");


def get_session(request):
    """得到session信息"""
    username = request.session["username"];
    age = request.session["age"];

    return HttpResponse("得到session的值" + username + str(age));


def clear_session(request):
    """清除session"""
    # 清除session 中部分键值
    del request.session["age"];
    # 清除所有的session 在存储中删除部分
    request.session.clear()
    # 清除所有的session 在存储中也全部删除
    request.session.flush()

    return HttpResponse('清除成功');


def templateLanguageBase(request):
    """模板语言基础"""

    dict_content = {'title': 'fan', 'age': 18, 'parent': True};
    list_content = ['fan', 'cnn', 'wdk', 'lyx', 'bb'];
    num_list = list(range(0, 10));
    users = UserInfo.objects.all();

    return render(request, 'loginfunction/templateLanguageBase.html', {
        'dict_content': dict_content, 'list_content': list_content, 'users': users,
        'num_list': num_list
    });


def child_template(request):
    """模板继承的使用"""
    return render(request, 'loginfunction/child.html');


def excape(request):
    """转义"""
    return render(request, 'loginfunction/excape.html', {
        'content': '<h1>I love you</h1>',
        'content1': '&lth1&gt I am very beautiful &lt/h1&gt'
    })


def url_reverse(request):
    """url 的反向解析"""

    return render(request, 'loginfunction/url_reverse.html');


def url_reverse_args(request, a, b):
    """带参数的反向url 解析"""
    return render(request, 'loginfunction/url_reverse_args.html', {'content': (a, b,)})


def url_reverse_argsname(request, a, b):
    """带参数的反向url 解析"""
    return render(request, 'loginfunction/url_reverse_args.html', {'content': (a, b,)})


def get_authcode(request):
    """获取验证码"""

    # buf_value 这个是验证码图片数据 auth_code 这个是验证码

    buf_value, auth_code = public_pac.get_authcode_picture();

    # 这个是返回给客户端的数据 数据mime类型为png
    return HttpResponse(buf_value, 'image/png');


def show_authcode(request):
    """返回验证码"""
    return render(request, 'loginfunction/show_authcode.html');


from django.urls import reverse


def test_view_redirect(request):
    """测试视图的反向解析"""
    # 重定向到 redirect('/index');
    url = reverse('loginfunction:index');

    # 重定向到/show_args/1/2
    url = reverse('loginfunction:show_args', args=(1, 2));

    # 重定向到/show_kwargs/3/4
    url = reverse('loginfunction:show_kwargs', kwargs={'c': 3, 'd': 4});

    return redirect(url);


def show_args(request, a, b):
    return render(request, 'loginfunction/url_reverse_args.html', {"content": (a, ':', b)});


def show_kwargs(request, c, d):
    return render(request, 'loginfunction/url_reverse_args.html', {"content": (c, ':', d)});


def static_file_image(request):
    """静态文件的使用"""
    return render(request,'loginfunction/static_file_image.html');

def get_computer_ip(request):
    """获取电脑的ip"""
    user_ip = request.META['REMOTE_ADDR'];

    return HttpResponse(user_ip);

def refuse_ip(request):
    """拒绝某一个ip的访问"""
    # 这个是要拒绝的ip地址list
    REFUSE_IPS = ['192.168.1.23'];

    # 获取访问的ip
    user_ip = request.META["REMOTE_ADDR"];

    if user_ip in REFUSE_IPS:
        return HttpResponse("你的ip被我们禁止了");

    return HttpResponse("正常访问");

def block_ip(view_func):

    def wrapper(request,*args,**kwargs):
        # 获取访问的ip
        user_ip = request.META["REMOTE_ADDR"];
        REFUSE_IPS = ['192.168.1.23'];
        if user_ip in REFUSE_IPS:
            return HttpResponse("你的ip被我们禁止了");
        else:
            return view_func(request,*args,**kwargs);

    return wrapper;


def middleware_exe(request):

    rep = HttpResponse('I am very well');

    def render():
        print('index ｂｅｆｏｒｅ')
        return HttpResponse('index');

    #  对象属性
    rep.render = render;

    return rep;

    return

# /pic_upload
def pic_upload(request):
    """这个是图片上传界面"""
    return render(request,'loginfunction/pic_upload.html');

# /upload_handle
def upload_handle(request):
    """图片上传处理函数"""
    # 1.get file upload object
    pic = request.FILES['pic'];

    # 2.create a file
    save_path = '%s/loginfunction/%s' % (settings.MEDIA_ROOT,pic.name);

    # 3.get upload file content and write new create file
    with open(save_path,'wb+') as f:
        for content in pic.chunks():
            f.write(content);


    # 4.save record in database
    TestPic.objects.create(pic='loginfunction/%s'%pic.name);
    # 5.return
    return HttpResponse("upload picture ok!");

from django.core.paginator import Paginator
def paging_use(reqeust,index):
    """分页"""
    # １．get data
    data = UserInfo.objects.all();

    # 2. every paging show ten
    paginator = Paginator(data,10);

    # 3.get paging data
    if not index:
        index = 1;
    pag = paginator.page(int(index));

    return render(reqeust,'loginfunction/paging_use.html',{"pag":pag})

def area_select(request):
    """城市选择器"""

    return render(request,'loginfunction/area_select.html')

def province(request):
    """查询省的数据"""
    # 1.查询数据
    province = AreaData.objects.filter(parent_id='0')

    # 2.构建JSON 数据
    area_list = [];

    for area in province:
        area_list.append((area.area_id,area.area_title));

    # 3.返回数据
    return JsonResponse({'data':area_list});

# /city/(\d+)
def city(request,area_id):
    """This is city' data"""

    # 1.query data
    area_data = AreaData.objects.filter(parent_id=area_id);

    # 2.make json data
    area_list = [];
    for area in area_data:
        area_list.append((area.area_id,area.area_title));

    # 3.return json data
    return JsonResponse({'data':area_list});






