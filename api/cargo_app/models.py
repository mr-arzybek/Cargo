from django.db import models


class GroupTrackCodes(models.Model):
    text_trackCode = models.CharField(max_length=300)
    track_codes = models.ManyToManyField('TrackCode', related_name='groups_track_codes', blank=True)
    statuses = models.ForeignKey('Status', related_name='groups_statuses', on_delete=models.CASCADE)
    date_group_created = models.DateTimeField()

    def date_format(self):
        return self.date_group_created.strftime('%d.%m.%Y')

    def __str__(self):
        return f'{self.statuses.name_status} and {self.text_trackCode}'

    class Meta:
        verbose_name = 'Группу Трек-кодов'
        verbose_name_plural = 'Группы Трек-кодов'


class Status(models.Model):
    name_status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name_status} {self.pk}'

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказов'


class TrackCode(models.Model):
    track_code_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.track_code_name} {self.pk}'

    class Meta:
        verbose_name = 'Код Заказа'
        verbose_name_plural = 'Коды Заказов'
