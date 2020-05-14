from django.db import models
from django.contrib.auth.models import User


class Liked(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image_href = models.CharField('Ссылка на страницу', max_length=300, db_index=True)

    def __str__(self):
        return f'{user}-{image_href}'
