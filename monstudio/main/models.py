from django.db import models
from django.utils import timezone


tz = timezone.get_default_timezone()


class feedback(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=12)
    txt = models.TextField('Отзыв', max_length=255)
    owner = models.CharField('Владелец', max_length=50)
    answer = models.TextField('Ответ', max_length=255)

    def __str__(self):
        return 'Отзыв от {}'.format(self.date.astimezone(tz).strftime('%d.%m.%Y %H:%M'))

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=12)
    txt = models.TextField('Сообщение', max_length=255)

    def __str__(self):
        return 'Сообщение от {}'.format(self.date.astimezone(tz).strftime('%d.%m.%Y %H:%M'))

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
