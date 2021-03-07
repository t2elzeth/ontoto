from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    path('api/catalog/', include('catalog.urls')),

    path('api/v1/', include('cart.urls')),
    path('api/favorites/', include('favorites.urls')),
    path('api/orders/', include('orders.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
