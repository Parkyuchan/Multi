# Generated by Django 4.2.3 on 2023-07-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='started_at',
            field=models.CharField(max_length=30),
        ),
    ]