# Generated by Django 4.2.3 on 2023-07-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_question_choice1_question_choice2_question_choice3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
