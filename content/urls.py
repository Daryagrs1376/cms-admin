from rest_framework.routers import DefaultRouter
from .views import ContentTypeViewSet, EntryViewSet


router = DefaultRouter()
router.register('content-types', ContentTypeViewSet)
router.register('entries', EntryViewSet)


urlpatterns = router.urls