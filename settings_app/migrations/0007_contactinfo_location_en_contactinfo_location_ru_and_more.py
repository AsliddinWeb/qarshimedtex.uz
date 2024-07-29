# Generated by Django 5.0.6 on 2024-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0006_headersettings_logo_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='location_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Manzil'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='location_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Manzil'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='location_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Manzil'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlinkcategory',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlinkcategory',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footerlinkcategory',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='copyright_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Mualliflik huquqi'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='copyright_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Mualliflik huquqi'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='copyright_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Mualliflik huquqi'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='bot_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Bot'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='bot_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Bot'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='bot_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Bot'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_alt_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Logo alt'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_alt_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Logo alt'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_alt_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Logo alt'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='right_button_title_en',
            field=models.CharField(max_length=50, null=True, verbose_name="O'ng tugma sarlavhasi"),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='right_button_title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name="O'ng tugma sarlavhasi"),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='right_button_title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name="O'ng tugma sarlavhasi"),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='search_placeholder_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Qidiruv matni'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='search_placeholder_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Qidiruv matni'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='search_placeholder_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Qidiruv matni'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='author_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Muallif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='author_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Muallif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='author_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Muallif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='keywords_en',
            field=models.TextField(null=True, verbose_name="Kalit so'zlar"),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='keywords_ru',
            field=models.TextField(null=True, verbose_name="Kalit so'zlar"),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='keywords_uz',
            field=models.TextField(null=True, verbose_name="Kalit so'zlar"),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='socialsettings',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='socialsettings',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='socialsettings',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
    ]
