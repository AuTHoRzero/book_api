from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .tasks import *

# Create your models here.


# В модель пользователя не было внесено изменений, тк необходимые поля, а именно:
# - Имя пользователя
# - Эл. почта
# - Дата регистрации
# Присутствуют в этом классе по умолчанию
class ApiUser(AbstractUser):
    '''
    User model
    '''

    class Meta:
        verbose_name = 'API Пользователь'
        verbose_name_plural = 'API пользователи'

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        send_hello_massage(self.email)
        super(ApiUser, self).save(*args, **kwargs)


class Book(models.Model):
    name = models.CharField(verbose_name='Наименование')
    author = models.CharField(verbose_name='Автор')
    publicate_date = models.DateField(verbose_name='Дата публикации')
    isbn = models.CharField(verbose_name='ISBN', max_length=20)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return self.name
    