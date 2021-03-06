from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LabType(models.Model):
    type_name = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.type_name
    
class Lab(models.Model):
    title = models.CharField(max_length = 50)
    lab_type = models.ForeignKey(LabType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated_time = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '<Lab: %s>' % self.title
    
    