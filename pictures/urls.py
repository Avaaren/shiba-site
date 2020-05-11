from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetShibaImage.as_view(), name = 'main_page'),
]