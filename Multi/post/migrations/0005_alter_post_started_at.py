# Generated by Django 4.2.3 on 2023-08-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_started_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='started_at',
            field=models.CharField(max_length=30),
        ),
    ]