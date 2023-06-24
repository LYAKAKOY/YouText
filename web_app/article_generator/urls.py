from django.conf.urls.static import static
from django.urls import path
from config import settings
from .views import generator

urlpatterns = [
    path('generator/', generator, name='generator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
