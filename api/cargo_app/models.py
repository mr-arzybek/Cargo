from django.db import models


class Status(models.Model):
    name_status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name_status} {self.pk}'

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказов'


class TrackCode(models.Model):
    track_code = models.CharField(max_length=200, unique=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.track_code} {self.pk}'

    def date_format(self):
        return self.date.strftime('%d.%m.%Y')

    class Meta:
        verbose_name = 'Код Заказа'
        verbose_name_plural = 'Коды Заказов'

