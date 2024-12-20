# Generated by Django 5.0.6 on 2024-07-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0017_contactus_bot_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ism')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon')),
                ('message', models.TextField(verbose_name='Xabar')),
                ('is_view', models.BooleanField(default=False, verbose_name="Ko'rilganmi?")),
            ],
            options={
                'verbose_name': '7. Xabarlar',
                'verbose_name_plural': '7. Xabarlar',
            },
        ),
    ]
