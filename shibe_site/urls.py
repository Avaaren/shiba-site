from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('pictures.urls')),
    path('account/', include('account.urls')),
    path('like/', include('likes.urls')),
]
