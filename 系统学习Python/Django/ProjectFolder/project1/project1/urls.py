"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pat
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
# 这是老版本的导入方式，新版本的方式不用URL，用path
from django.conf.urls import include,url

# 项目的urls 配置文件,也可以配合着路径
urlpatterns = [
    path('admin/', admin.site.urls),
   # re_path('booktest/',include('booktest.urls')),

    url("^",include('booktest.urls'))
]
