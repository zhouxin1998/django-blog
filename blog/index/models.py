from django.db import models
from tinymce.models import HTMLField
# from ..login.models import UserInfo
# from rte import RTEField
# Create your models here.
class TypeInfo(models.Model):
    # 标题
    tTitle = models.CharField(max_length=20)
    # 是否逻辑删除
    tIsDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.tTitle

class BowenInfo(models.Model):
    # 文章标题
    bTitle = models.CharField(max_length=30)
    # 文章图片
    bPic = models.ImageField(upload_to='bowen_img',blank=True)
    # 文章内容
    bContent = HTMLField()
    #发布时间
    bDate = models.DateTimeField(auto_now_add=True)
    #点击量
    bClick = models.IntegerField(default=0)
    #评论量
    bComment = models.IntegerField(default=0)
    # 是否逻辑删除
    bIsDelete = models.BooleanField(default=False)
    # 是否置顶
    bIstop = models.BooleanField(default=False)
    # 添加外建约束
    bType = models.ForeignKey(TypeInfo,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.bTitle
