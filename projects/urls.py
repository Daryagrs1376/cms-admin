from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectMembershipViewSet
from django.urls import path, include



router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('memberships', ProjectMembershipViewSet)


urlpatterns = [
    path('', include(router.urls)),
]