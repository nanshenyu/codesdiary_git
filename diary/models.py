from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DiaryType(models.Model):
    type_name = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.type_name
    
class Diary(models.Model):
    
    #标题
    title = models.CharField(max_length = 50)
    #日记-类型
    diary_type = models.ForeignKey(DiaryType, on_delete=models.DO_NOTHING)
    #内容
    content = models.TextField()
    #作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #创建时间
    created_time = models.DateTimeField(auto_now_add = True)
    #更新时间
    last_updated_time = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '<Diary: %s>' % self.title
    
    class Meta:
        ordering = ['-created_time']
