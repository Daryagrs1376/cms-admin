from django.db import models
from projects.models import Project


class ContentType(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200)  
    schema = models.JSONField(null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name 

#این فیلدschemaبرای اینه که هرپروژه مدلهاشو بتونه بصورت schema تعریف کنه 
#یعنی داده های واقعی داشته باشه

class Entry(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    data = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
