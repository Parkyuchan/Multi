# Generated by Django 4.2.3 on 2023-07-25 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_old_man_remove_volunteer_old_man_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Old_man',
            new_name='Needed_man',
        ),
        migrations.RenameField(
            model_name='needed_man',
            old_name='old_man',
            new_name='needed',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='old_man',
            new_name='needed',
        ),
    ]
