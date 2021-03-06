from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('cart', views.CartViewSet)

urlpatterns = router.urls
