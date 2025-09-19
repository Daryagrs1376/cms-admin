from rest_framework import viewsets
from .models import ContentType, Entry
from .serializers import ContentTypeSerializer, EntrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions



class ContentTypeViewSet (viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [DjangoModelPermissions]
    #permission_classes فقط کاربرهایی که دسترسی دارن (مثلاً ادمین) می‌تونن بهش لاگین دسترسی داشته باشن.


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [DjangoModelPermissions]
    
    
    def get_queryset(self):
#اگر کاربر ادمین نیست، فقط محتوای مربوط به پروژه‌های خودش را ببیند.
#یعنی برای مشخص کردن اینکه کدوم داده‌ها به کدوم پروژه مربوط میشه، باید از اطلاعات عضویت پروژه کاربر استفاده کنیم.

        user = self.request.user #اگه لاگین کرده باشه، اطلاعاتش رو می‌ده
        qs = Entry.objects.all() #تمام ورودی‌ها رو می‌گیره

        if user.is_superuser: #اگر کاربر ادمین باشد
            return qs #تمام ورودی‌ها رو برمی‌گردونه

        project_ids = user.projectmembership_set.values_list('project_id', flat=True)
#لیست پروژهایی که کاربر داخلش عضوه بصورت لیست میده
#برای محدود کردن دسترسی کاربر به پروژه‌های خاص

        return qs.filter(content_type__project_id__in=project_ids)
#برای محدود کردن دسترسی کاربر به پروژه‌های خاص

#متد get_queryset تو EntryViewSet اینجوری کار می‌کنه:
#اگر کاربر سوپر‌یوزر باشه، همه Entryها رو نشون می‌ده.
#اگر نه، فقط Entryهایی رو برمی‌گردونه که به پروژه‌هایی ربط دارن که کاربر توش عضوه