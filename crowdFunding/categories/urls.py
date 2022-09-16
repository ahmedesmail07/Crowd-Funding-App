from django.urls import path
from categories.views import CreateCategory


urlpatterns = [
    path('create', CreateCategory.as_view(), name="createCategory")
]
