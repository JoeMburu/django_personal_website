from django.urls import path, include
from .views import projects

urlpatterns = [
    path('', projects, name='projects'),
]
