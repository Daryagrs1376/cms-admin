from rest_framework import viewsets
from .models import Project, ProjectMembership
from .serializers import ProjectSerializer, ProjectMembershipSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    

class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer