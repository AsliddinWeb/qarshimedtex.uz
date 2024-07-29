# Generated by Django 5.0.6 on 2024-07-01 13:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_alter_homecourses_options_homecourses_hover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecourses',
            name='hover_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='courses_images/', verbose_name='Hover rasmi'),
            preserve_default=False,
        ),
    ]
