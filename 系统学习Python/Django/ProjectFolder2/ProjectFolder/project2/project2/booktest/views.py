from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date
# 这个是用来做重定向的
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def show_books(request):
    """显示图书列表"""
    # 1.获取图书列表数据
    books = BookInfo.objects.all();
    return render(request, 'booktest/show_books.html', {"books": books});


def add_book(request):
    """添加图书"""
    book = BookInfo();
    book.btitle = "西游记";
    book.bpub_date = date(1991,1,2);
    book.save();

    # 反应完成，让浏览器 再吃访问同一页面 这个也叫作重定向
    return HttpResponseRedirect('/index');

def delete_book(reuestet, bid):
    """删除图书"""
    print('I love you')
    book = BookInfo.objects.get(id=bid);
    print(str(bid));
    book.delete();

    return HttpResponseRedirect('/index');