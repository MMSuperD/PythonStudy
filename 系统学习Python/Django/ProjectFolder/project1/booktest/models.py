from django.db import models

# Create your models here.

# 图书类
class BookInfo(models.Model):
    ''''图书模型类'''
    # 图书名称 CharField 说明是一个字符串 max_length 表示最大的长度为20
    btitle = models.CharField(max_length=20);
    # 出版日期
    bpub_date = models.DateField();

    # 重写魔法方法，返回书名（默认返回的是对象本身）
    def __str__(self):
        return self.btitle;

# 英雄人物类
class HeroInfo(models.Model):
    '''英雄类'''
    # 姓名：
    hname = models.CharField(max_length=20);
    # 性别：默认为 女性false
    hgender = models.BooleanField(default=False);
    # 备注：
    hcomment = models.CharField(max_length=128);
    # 所在图书  关系表中对应表中的字段名字：关系属性名字_id
    # 一对多设计　多方持有一方的外键
    hhook = models.ForeignKey("BookInfo",on_delete=models.CASCADE);

    # 重写魔法方法，返回英雄名（默认返回的是对象本身）
    def __str__(self):
        return self.hname;