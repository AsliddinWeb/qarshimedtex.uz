# Generated by Django 5.0.6 on 2024-07-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0011_newsdetailtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdetailtext',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='newsdetailtext',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='newsdetailtext',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
    ]
