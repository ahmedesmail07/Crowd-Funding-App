from django.shortcuts import render
from projects.models import Category
from categories.forms import CategoryModelForm
from django.views.generic.edit import CreateView
# Create your views here.


class CreateCategory(CreateView):
    form_class = CategoryModelForm
    template_name = 'categories/createCategory.html'
    success_url = '/'