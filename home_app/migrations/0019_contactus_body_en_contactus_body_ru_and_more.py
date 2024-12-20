# Generated by Django 5.0.6 on 2024-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0018_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Tana Matni'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Tana Matni'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Tana Matni'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='cap_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='cap_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='cap_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_en',
            field=models.TextField(null=True, verbose_name='Xabar'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_ru',
            field=models.TextField(null=True, verbose_name='Xabar'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_uz',
            field=models.TextField(null=True, verbose_name='Xabar'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faq',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='faq',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='faq',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='cap_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='cap_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='cap_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='faqtitle',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='alt_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='alt_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='alt_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_1_en',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_1_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_1_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_2_en',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_2_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_2_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik matni'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='cap_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='cap_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='cap_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='count_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sanoq Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='count_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sanoq Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='count_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sanoq Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='quote_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Iqtibos'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='quote_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Iqtibos'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='quote_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Iqtibos'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_1_en',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_1_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_1_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_2_en',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_2_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_2_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='1 - Qulaylik'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='two_body_en',
            field=models.TextField(null=True, verbose_name='Ikkinchi Matn'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='two_body_ru',
            field=models.TextField(null=True, verbose_name='Ikkinchi Matn'),
        ),
        migrations.AddField(
            model_name='homeabout',
            name='two_body_uz',
            field=models.TextField(null=True, verbose_name='Ikkinchi Matn'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='cap_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='cap_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='cap_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homecourses',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Lavozim'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Lavozim'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='position_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Lavozim'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism familiya'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism familiya'),
        ),
        migrations.AddField(
            model_name='homeleader',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Ism familiya'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='courses_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kurslar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='faq_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='FAQ sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='liders_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Liderlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news2_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Ikkinchi yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='news_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Yangiliklar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_cap_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_cap_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_cap_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar kichik sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='hometitles',
            name='partners_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Hamkorlar sarlavhasi'),
        ),
        migrations.AddField(
            model_name='partner',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='partner',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='partner',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='slider',
            name='body_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='slider',
            name='button_text_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Tugma Matni'),
        ),
        migrations.AddField(
            model_name='slider',
            name='button_text_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Tugma Matni'),
        ),
        migrations.AddField(
            model_name='slider',
            name='button_text_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Tugma Matni'),
        ),
        migrations.AddField(
            model_name='slider',
            name='cap_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='cap_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='cap_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Kichik Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image_alt_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image_alt_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image_alt_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Rasm Tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
    ]
