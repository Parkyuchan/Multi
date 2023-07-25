# Generated by Django 4.2.3 on 2023-07-25 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_user_needed_delete_needed_man'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
