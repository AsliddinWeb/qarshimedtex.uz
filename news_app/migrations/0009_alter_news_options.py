# Generated by Django 5.0.6 on 2024-07-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0008_remove_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
    ]
