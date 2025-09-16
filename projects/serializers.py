from rest_framework import serializers
from .models import Project, ProjectMembership



class ProjectMembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    
    class Meta:
        model = ProjectMembership
        fields =['user', 'role']
        
        

class ProjectSerializer(serializers.ModelSerializer):
    memberships = ProjectMembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields =['id', 'name', 'description', 'memberships']