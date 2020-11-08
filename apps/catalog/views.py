from django.shortcuts import render
from django.views import View

from . import models

# Create your views here.
class CategoriesAllView(View):
    def get(self, request):
        queryset = models.Category.objects.all()
        context = {
            'queryset': queryset
        }
        return render(request, 'catalog/index.html', context)