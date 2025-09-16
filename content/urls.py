from rest_framework.routers import DefaultRouter
from .views import ContentTypeViewSet, EntryViewSet


router = DefaultRouter()
router.register('content-types', ContentTypeViewSet, basename='ContentType')
router.register('entries', EntryViewSet, basename='Entry')


urlpatterns = router.urls