from django.contrib import admin

from .models import Liked


@admin.register(Liked)
class LikedAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'image_href']
# Register your models here.
