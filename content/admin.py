from django.contrib import admin
from .models import ContentType, Entry


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'created_at')
    list_filter = ('project') #برای این قرار دادم که وقتی تعداد پروژه ها زیاد شد این فیلتر کار مدیر راحت کنه


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'created_at')
    list_filter = ('content_type__project', 'content_type')
    fields = '__all__'
