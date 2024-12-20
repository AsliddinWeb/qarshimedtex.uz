# Generated by Django 5.0.6 on 2024-07-25 17:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='page',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='page',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='page',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Sarlavha'),
        ),
    ]
