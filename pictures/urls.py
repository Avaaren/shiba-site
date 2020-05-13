from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetShibaImage.as_view(), name='main_page'),
    
    path('download/',
         views.DownloadClickHandle.as_view(),
         name='download_click'),

    path('download/<str:filename>',
         views.DownloadFileView.as_view(),
         name='save_file')
]
