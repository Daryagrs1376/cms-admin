from rest_framework import viewsets, permissions
from content.models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project = self.request.query_params.get('project')
        qs = Entry.objects.all()
        if project:
            qs = qs.filter(content_type__project__name=project)
        return qs