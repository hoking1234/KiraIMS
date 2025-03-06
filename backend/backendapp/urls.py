from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

raw_patterns = []


if settings.ADMIN_ENABLED:
    raw_patterns = [
        path("admin/", admin.site.urls),
    ]
raw_patterns += [
    path("", include("backendapp.apps.inventory.urls", namespace="inventory")),
]

if settings.DEBUG:
    raw_patterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    raw_patterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

urlpatterns = raw_patterns
