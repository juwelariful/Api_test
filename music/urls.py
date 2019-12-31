
from django.urls import path, include
from .views import ListSongsView

urlpatterns = [
    path('song/', ListSongsView.as_view(), name='song'),
]
