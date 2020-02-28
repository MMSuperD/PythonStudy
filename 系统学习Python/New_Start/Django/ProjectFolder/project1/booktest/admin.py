from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    """自定义图书模型管理类"""
    list_display = ['id','btitle','bpub_date'];


class HeroInfoAdmin(admin.ModelAdmin):
    """自定义英雄模型管理类"""
    list_display = ['id','hname','hgender','hcomment','hhook'];

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin);
admin.site.register(HeroInfo,HeroInfoAdmin);
