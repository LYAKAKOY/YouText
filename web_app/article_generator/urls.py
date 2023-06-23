from django.urls import path
from .views import generator

urlpatterns = [
    path('generator/', generator, name='generator'),
]
