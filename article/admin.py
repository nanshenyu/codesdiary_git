from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin (admin.ModelAdmin):
    #界面列表显示
    list_display = ('id','title','content','author','readed_num','created_time','last_updated_time')
    #排序
    ordering = ('id',)

#admin.site.register(Article,ArticleAdmin)