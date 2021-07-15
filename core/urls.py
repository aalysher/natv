from django.urls import path
from . import views

urlpatterns = [
    path('channel/', views.get_channels)
]
