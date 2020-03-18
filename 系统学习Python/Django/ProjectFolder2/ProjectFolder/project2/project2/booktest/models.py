from django.db import models
from datetime import date

# Create your models here.

class BookInfo(models.Model):
    """图书简介属性"""
    # 图书名
    btitle = models.CharField(max_length=20);

    # 出版日期
    bpub_date = models.DateField();

    # 阅读数
    bread = models.IntegerField(default=0);

    # 评论数
    bcomment = models.IntegerField(default=0);

    # 是否删除
    isDelete = models.BooleanField(default=False);

    def __str__(self):
        return self.btitle;


class HeroInfo(models.Model):
    """图书简介属性"""
    # 英雄名字
    hname = models.CharField(max_length=20);

    # 英雄性别
    hgender = models.BooleanField(default=False);

    # 关联书籍
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE);

    # 精通技能
    hcomment = models.CharField(max_length=20);

    # 是否删除
    isDelete = models.BooleanField(default=False);

    def __str__(self):
        return self.hname;