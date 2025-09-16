from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProjectMembership(models.Model):
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('editor', 'Editor'),
        ('manager', 'Manager'),
    ]
    
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    
    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} - {self.project} ({self.role})"