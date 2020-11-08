from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriesAllView.as_view())
]