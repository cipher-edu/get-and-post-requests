from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', home),
    path('cats/<int:catid>/', categorey),
    path('404/', notfound, name='404'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]