# Generated by Django 4.2.3 on 2023-08-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1, max_length=200),
            preserve_default=False,
        ),
    ]
