# Generated by Django 4.2.6 on 2023-11-22 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0007_remove_grouptrackcodes_track_codes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouptrackcodes',
            old_name='statuses',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='grouptrackcodes',
            name='track_codes',
        ),
        migrations.AddField(
            model_name='grouptrackcodes',
            name='group_track_code',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackcode',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='track_codes', to='cargo_app.grouptrackcodes'),
            preserve_default=False,
        ),
    ]
