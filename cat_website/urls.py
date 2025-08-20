from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# This block is crucial for serving media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)