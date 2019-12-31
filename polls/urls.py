
from django.urls import path
from .views import PollView
urlpatterns = [
    path('polls/',PollView.as_view(), name='poll_list'),
    path('polls/<int:id>/',PollView.as_view(), name='poll_details'),
]
