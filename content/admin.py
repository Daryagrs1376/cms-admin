from django.contrib import admin
from .models import ContentType, Entry
from guardian.admin import GuardedModelAdmin
import reversion
from reversion.admin import VersionAdmin



@admin.register(ContentType)
class ContentTypeAdmin(GuardedModelAdmin):
    list_display = ['name', 'project', 'created_at']
    list_filter = ['project'] 


@admin.register(Entry)
class EntryAdmin(GuardedModelAdmin, reversion.admin.VersionAdmin):
    list_display = ['id', 'content_type', 'created_at']
    list_filter = ['content_type__project', 'content_type']