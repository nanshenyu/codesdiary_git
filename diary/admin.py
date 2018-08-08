from django.contrib import admin
from .models import DiaryType,Diary

# Register your models here.

@admin.register(DiaryType)
class DiaryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diary_type', 'author', 'created_time','last_updated_time')