# Generated by Django 4.2.3 on 2023-08-13 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_post_followings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_follow',
        ),
    ]
