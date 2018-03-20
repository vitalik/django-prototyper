import os
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .views import main_view, api_build, api_save, discover_plugins, install_plugin


urlpatterns = (
    path('', main_view),
    path('api/build/', api_build),
    path('api/save/', api_save),
    path('api/plugin/', discover_plugins),
    path('api/plugin/install/', install_plugin),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'static')}),
)
