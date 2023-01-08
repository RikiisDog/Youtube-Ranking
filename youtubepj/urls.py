from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_PATH + '/' , admin.site.urls),
    path('', include('youtubeapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
