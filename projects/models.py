from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()
#از مدل کاستم یوزر استفاده کردم که اگر بعد مدل کاربرم تغیر کرد
#کدهام خراب نشه

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# __str__ برای صدا کردن اسم پروژه


class ProjectMembership(models.Model):
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('editor', 'Editor'),
        ('manager', 'Manager'),
    ]
#به مدل کاستوم یوزر فارنکیه اگر کاربر حذف بشه اطلاعاتش حذف میشه 
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    
    class Meta:
        unique_together = ('user', 'project')
#این کوئری برای این زدم که هرکس فقط یبار به پروژه وصل شه ن دوبار
#کمک میکنه اطلاعات تکراری وارد نشن

    def __str__(self):
        return f"{self.user} - {self.project} ({self.role})"
#self.user: نمایش نام کاربر عضو پروژه.
#self.project: نمایش نام پروژه‌ای که کاربر عضو آن است.
#self.role: نقش کاربر در پروژه (مانند viewer، editor یا manager).