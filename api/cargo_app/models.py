from django.db import models

class Status(models.Model):
    name_status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name_status

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказов'


class TrackCode(models.Model):
    track_code_name = models.CharField(max_length=200, unique=True)
    group = models.ForeignKey(
        "GroupTrackCodes",
        on_delete=models.CASCADE,
        related_name='track_codes'  # This is the line you need to add or modify
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.track_code_name

    class Meta:
        verbose_name = 'Код Заказа'
        verbose_name_plural = 'Коды Заказов'

class GroupTrackCodes(models.Model):
    text_trackCode = models.CharField(max_length=300)
    status = models.ForeignKey(Status, related_name='groups_statuses', on_delete=models.CASCADE)
    date_group_created = models.DateTimeField()
    group_track_code = models.CharField(max_length=300)

    def date_format(self):
        return self.date_group_created.strftime('%d.%m.%Y')


    class Meta:
        verbose_name = 'Группу Трек-кодов'
        verbose_name_plural = 'Группы Трек-кодов'
