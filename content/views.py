from rest_framework import viewsets
from .models import ContentType, Entry
from .serializers import ContentTypeSerializer, EntrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions




class ContentTypeViewSet (viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [DjangoModelPermissions]


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [DjangoModelPermissions]
    
    
    def get_queryset(self):
        user = self.request.user
        qs = Entry.objects.all()
        
        if user.is_superuser:
            return qs
        
        
        project_ids = user.projectmembership_set.values_list('project_id', flat=True)
        return qs.filter(content_type__project_id__in=project_ids)