from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view()),
    path('create/', views.ProductCreateView.as_view()),
    path('detail/<str:pk>/', views.ProductDetailView.as_view()),
]
