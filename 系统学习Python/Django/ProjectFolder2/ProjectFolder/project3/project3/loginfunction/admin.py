from django.contrib import admin

from loginfunction.models import UserInfo

class UserAdmin(admin.ModelAdmin):

    #  ｉｄ，ｕｓｅｒｎａｍｅ，ｇｅｎｄｅｒ是属性，ｔｉｔｌｅ是方法
    list_display = ['id','username','gender','title'];
    list_per_page = 10; # 这个是每页显示多少条数据
    actions_on_bottom = True;
    actions_on_top = False;

    list_filter = ['username'];  # 列表右侧过滤栏
    search_fields = ['username'];  # 列表上方搜索栏

    fieldsets = (
        ('基本信息',{'fields':['username']}),
        ('性别', {'fields':['gender']}),
    );

admin.site.register(UserInfo,UserAdmin);