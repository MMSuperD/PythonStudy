# 这是老版本的导入方式，新版本的方式不用URL，用path
from django.conf.urls import include,url
from loginfunction import views

urlpatterns = [
    url('^login/?$',views.login),
    url('^ajax_login$',views.ajax_login),
    url('^index$',views.index,name='index'),

    url('^set_cookie$',views.set_cookie), # 这个是设置cookie的值
    url('^get_cookie$',views.get_cookie), # 这里是得到 cookie的值
    url('^set_session$',views.set_session), # 这个是设置session的值
    url('^get_session$',views.get_session), # 这里是得到 session的值

    url('^templateLanguageBase$',views.templateLanguageBase), # 模板语言基础用法

    url('^child$',views.child_template), # 模板继承使用
    url('^excape$',views.excape),  # 转义的使用

    url('^url_reverse$',views.url_reverse),  # url 的反向解析

    url('^url_reverse_args/(\d+)/(\d+)$',views.url_reverse_args,name='url_reverse_args'),

    url('^url_reverse_argsname/(?P<a>\d+)/(?P<b>\d+)$', views.url_reverse_argsname, name='url_reverse_argsname'),

    url('^get_authcode$',views.get_authcode),

    url('^show_authcode$',views.show_authcode),  # 显示验证码

    url('^test_view_redirect$',views.test_view_redirect),  # 测试视图反向解析

    url('^show_args/(\d+)/(\d+)$',views.show_args,name='show_args'),  # 测试带参数的反向解析

    url('^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$', views.show_kwargs,name='show_kwargs'),  # 测试带参数的反向解析

    url('^static_file_image$',views.static_file_image),  # 这个是静态文件使用图片

    url('^get_computer_ip$',views.get_computer_ip),  # 获取电脑的ip地址

    url('^refuse_ip$',views.refuse_ip),  # 拒绝某一个ip的请求

    url('^middleware_exe$',views.middleware_exe),  # 中间件函数的执行

    url('^pic_upload$',views.pic_upload),  # 图片上传界面

    url('^upload_handle$',views.upload_handle),  # 图片上传处理函数

    url('^paging_use/(?P<index>\d*)$',views.paging_use),  # 分页数据显示

    url('^area_select$',views.area_select),  # 地区选择

    url('^province$',views.province),   # 这个是省的数据

    url('^city/(?P<area_id>\d+)',views.city),  # 这个是城市的数据

]