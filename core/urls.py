from django.urls import path
from . import views

urlpatterns = [
    path('channel/', views.ChannelList.as_view())
]
