# Generated by Django 4.2.3 on 2023-08-13 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': '카테고리',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('manu_f', models.CharField(blank=True, max_length=50)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('price_buy', models.CharField(blank=True, max_length=50)),
                ('price_borrow', models.CharField(blank=True, max_length=50)),
                ('url_go', models.URLField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
        ),
    ]
