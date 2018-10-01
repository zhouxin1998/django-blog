from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 用户名
    uName = models.CharField(max_length=20)
    # 手机号
    uPhone = models.CharField(max_length=20)
    # 邮箱
    uEmail = models.CharField(max_length=20)
    # 密码
    uPassword = models.CharField(max_length=20)