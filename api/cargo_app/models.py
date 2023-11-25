from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=300)
    status = models.ForeignKey('Status', related_name='groups', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.status.name_status}'

    def date_format(self):
        return self.date.strftime('%Y-%m-%d')
    class Meta:
        verbose_name = 'Группу Трек-кодов'
        verbose_name_plural = ('Группы Трек-кодов')

class Status(models.Model):
    name_status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name_status} {self.pk}'

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказов'


class TrackCode(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='track_codes')
    track_code = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.track_code} {self.pk}'

    class Meta:
        verbose_name = 'Код Заказа'
        verbose_name_plural = 'Коды Заказов'
