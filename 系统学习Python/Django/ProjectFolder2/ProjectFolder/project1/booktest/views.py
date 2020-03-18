from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo
# Create your views her

#1.定义视图函数，返回响应体
#2.进行url配置，进行url地址和视图的对应关系
# 117.0.0.1:8000/index

def index(request):
    # 进行处理M 和 T 的交互
    #1.加载模板文件
    template_file = loader.get_template("booktest/index.html");
    #2.定义模板上线文，给模板传递数据
    template_context = RequestContext(request,{});
    #3.渲染模板，把模板中的变量等转化为标准的html
    template_html = template_file.render(context=locals(), request=request);
    return HttpResponse(template_html);

def index2(request):
    # 这个是简写形式
    return render(request,"booktest/index.html",{});

def dynamicPage(request):
    # 这个是简写形式
    return render(request,"booktest/dynamicPage.html",{
        "content":"就是这么溜溜",
        "list":list(range(1,10)),
    });

def index_defalut(request):
    return render(request,"booktest/default.html",{});



#--------------------这个是图书列表的案例
def show_books(request,*callback_args):

    print("show_boos",callback_args);
    # 1.获取数据
    books = BookInfo.objects.all();

    # 返回标准的html5 模板
    return render(request,"booktest/book_list.html",{"books":books});

# 这个是图书详情界面
def show_book_detail(request,bid):
    # bid:传过来的参数 这个在路由url的时候，必须用组
    # 1.获取该本图书中，所涉及到的英雄 heroinfo_set 这个方法类名所有的字母都得小写
    heroes = BookInfo.objects.get(id=bid).heroinfo_set.all();
    print("bid",bid);
    # 返回标准的html5模板
    return render(request,"booktest/book_detail.html",{"heroes":heroes,"book":BookInfo.objects.get(id=bid)});
