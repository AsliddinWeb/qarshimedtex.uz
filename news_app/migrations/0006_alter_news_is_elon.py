# Generated by Django 5.0.6 on 2024-06-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_news_is_elon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_elon',
            field=models.BooleanField(default=False, verbose_name="Bu e'lon"),
        ),
    ]
