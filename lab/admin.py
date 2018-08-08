from django.contrib import admin
from .models import LabType,Lab

# Register your models here.

@admin.register(LabType)
class LabTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('title', 'lab_type', 'author', 'created_time','last_updated_time')