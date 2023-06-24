from django.conf.urls.static import static
from django.urls import path
from config import settings
from .views import generator, logout_social

urlpatterns = [
    path('', generator, name='generator'),
    path('logout/', logout_social, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
