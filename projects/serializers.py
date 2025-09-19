from rest_framework import serializers
from .models import Project, ProjectMembership



class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    #read_only=True یعنی این فیلد فقط برای خوندن
    #StringRelatedFieldاستفاده کردم که باتوجه به fields فقط اسم کاربر و نقشش نمایش داده بشه
    class Meta:
        model = ProjectMembership
        fields =['user', 'role']
        
        

class ProjectSerializer(serializers.ModelSerializer):
    memberships = ProjectMembershipSerializer(many=True, read_only=True)
    #many=True چون هر پروژه میتونه چندتا ProjectMembership داشته باشه این many=True
    #کل اطلاعات کاربرای پروژه بصورت لیست میده
    #اگر many=True نزارم خطا میده
    
    class Meta:
        model = Project
        fields =['id', 'name', 'description', 'memberships']
    #memberships لیست کاربرای پروژه نشون میده