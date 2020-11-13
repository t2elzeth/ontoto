from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CartProductCreateView.as_view())
]
