from django.urls import path

from . import views

urlpatterns = [
    path('', views.FavoriteProductListView.as_view()),
    path('create/', views.FavoriteProductCreateView.as_view()),
    path('detail/<str:pk>/', views.FavoriteProductDetailView.as_view()),
]
