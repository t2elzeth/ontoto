from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrdersListView.as_view()),
    path('create/', views.OrderCreateView.as_view()),
    path('detail/<str:pk>/', views.OrderRetrieveUpdateDestroyView.as_view()),
]
