# Generated by Django 4.2.3 on 2023-08-13 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_user_followings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
    ]
