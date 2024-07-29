# Generated by Django 5.0.6 on 2024-07-01 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0009_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='news_images/', verbose_name='Asosiy rasm'),
            preserve_default=False,
        ),
    ]