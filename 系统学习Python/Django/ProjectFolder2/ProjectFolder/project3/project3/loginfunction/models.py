from django.db import models

class UserInfo(models.Model):
    """用户信息表模型"""
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    gender   = models.BooleanField(verbose_name='性别',default=False);

    def __str__(self):
        return self.username;

    def title(self):
        """这个方法可以用来计算"""
        return self.username;
    title.admin_order_field = 'username';
    title.short_description = '姓名'


    class Meta:
        db_table = "userinfo";  # 这个是指定用户信息表的名字


class TestPic(models.Model):
    """图片上传模型"""
    pic = models.ImageField(upload_to='loginfunction');


class AreaData(models.Model):
    """地理模型"""
    # area id
    area_id = models.CharField(max_length=20);

    # title
    area_title = models.CharField(max_length=20);

    # parent id
    parent_id = models.CharField(max_length=20);

    class Meta:
        db_table = "area_data";