from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('syslogweb/', include('base.urls')),
    path('', include('authentication.urls')),
    path('accounts/', include('accounts.urls')),
    path('unidades/', include('unidades.urls')),
    path('controle/', include('controle.urls')),
    path('logs/', include('log.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

