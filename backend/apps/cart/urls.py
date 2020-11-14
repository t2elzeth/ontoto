from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartProductListView.as_view()),
    path('create/', views.CartProductCreateView.as_view()),
    path('detail/<str:pk>/', views.CartProductDetailView.as_view())
]
