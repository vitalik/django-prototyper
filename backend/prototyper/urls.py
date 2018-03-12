from django.urls import path, re_path
from django.http import HttpResponse
from .views import main_view, api_build, api_save, discover_plugins, install_plugin

from django.views.static import serve


urlpatterns = (
    path('', main_view),
    path('api/build/', api_build),
    path('api/save/', api_save),
    path('api/plugin/', discover_plugins),
    path('api/plugin/install/', install_plugin),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': '/code/frontend/dist/'}),
)
