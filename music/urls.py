
from django.urls import path, include
from .views import music

urlpatterns = [
    path('music/', music, name='music'),
]
