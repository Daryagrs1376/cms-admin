from django.db import models
from projects.models import Project



class ContentType(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200)  
    schema = models.JSONField(help_text="ساختار JSON محتوا") 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name 



class Entry(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    data = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
