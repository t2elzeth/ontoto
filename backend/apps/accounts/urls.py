from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('me', views.MeViewSet)

urlpatterns = [
    path('users/', include(router.urls))
]
