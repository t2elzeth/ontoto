from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('favorites', views.FavoriteProductViewSet)

urlpatterns = router.urls
