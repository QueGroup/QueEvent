from django.db import models


# Create your models here.
class Event(models.Model):
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['-published']

    title = models.CharField(max_length=50, verbose_name="Событие")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    event_type = models.ForeignKey('EventType', null=True, on_delete=models.PROTECT, verbose_name='Тип события')


class EventType(models.Model):
    class Meta:
        verbose_name = "Тип события"
        verbose_name_plural = 'Типы событий'
        ordering = ['name']

    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
