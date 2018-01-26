from django.urls import path
from django.http import HttpResponse
from .views import main_view, api_build, api_save


urlpatterns = (
    path('', main_view),
    path('api/build/', api_build),
    path('api/save/', api_save),
)
