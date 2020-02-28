
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import include,url
from booktest import views

# 项目的urls 配置文件,也可以配合着路径
urlpatterns = [
    #re_path("index",views.index),
    url("^index$",views.index),
    url("^index2$",views.index2),
    url("^dynamicPage$",views.dynamicPage),
    url("^books(/?)$",views.show_books),#设置组的时候，一定要设置响应函数的参数
    url("^books/(\d+)/$",views.show_book_detail),
    url("^",views.index_defalut)

]