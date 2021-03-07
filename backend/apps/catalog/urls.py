from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('catalog', views.ProductViewSet)

urlpatterns = router.urls
