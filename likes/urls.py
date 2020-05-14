from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToggleLikeView.as_view(), name='toggle_like'),
]