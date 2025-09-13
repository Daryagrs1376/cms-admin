from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from django.urls import path, include



router = DefaultRouter()
router.register('projects', ProjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
]