from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Slider(models.Model):
    cap_title = models.CharField(
        max_length=255,
        verbose_name=_("Kichik Sarlavha")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    body = models.TextField(
        verbose_name=_("Matn")
    )
    button_text = models.CharField(
        max_length=100,
        verbose_name=_("Tugma Matni")
    )
    button_link = models.CharField(
        max_length=255,
        verbose_name=_("Tugma Havolasi")
    )
    target = models.BooleanField(
        default=False,
        verbose_name=_("Yangi oynada ochilsinmi?")
    )

    image = models.ImageField(
        upload_to='slider_images/',
        verbose_name=_("Rasm")
    )
    image_alt = models.CharField(
        max_length=255,
        verbose_name=_("Rasm Tavsifi")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Yaratilgan vaqti")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Yangilangan vaqti")
    )

    class Meta:
        verbose_name = _("1. Slayder")
        verbose_name_plural = _("1. Slayderlar")

    def __str__(self):
        return self.title

class HomeAbout(models.Model):
    count = models.IntegerField(
        verbose_name=_("Sanoq")
    )
    count_title = models.CharField(
        max_length=255,
        verbose_name=_("Sanoq Sarlavhasi")
    )
    image = models.ImageField(
        upload_to='about_images/',
        verbose_name=_("Rasm")
    )
    alt = models.CharField(
        max_length=255,
        verbose_name=_("Rasm Tavsifi")
    )
    cap_title = models.CharField(
        max_length=255,
        verbose_name=_("Kichik Sarlavha")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    body = models.TextField(
        verbose_name=_("Matn")
    )

    title_1 = models.CharField(
        max_length=255,
        verbose_name=_("1 - Qulaylik")
    )
    body_1 = models.CharField(
        max_length=255,
        verbose_name=_("1 - Qulaylik matni")
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name=_("1 - Qulaylik")
    )
    body_2 = models.CharField(
        max_length=255,
        verbose_name=_("1 - Qulaylik matni")
    )

    two_body = models.TextField(
        verbose_name=_("Ikkinchi Matn")
    )
    quote = models.CharField(
        max_length=255,
        verbose_name=_("Iqtibos")
    )

    class Meta:
        verbose_name = _("2. Biz Haqimizda")
        verbose_name_plural = _("2. Biz Haqimizda")

    def __str__(self):
        return self.title

class HomeTitles(models.Model):
    news_cap = models.CharField(
        max_length=255,
        verbose_name=_("Yangiliklar kichik sarlavhasi")
    )
    news_title = models.CharField(
        max_length=255,
        verbose_name=_("Yangiliklar sarlavhasi")
    )
    courses_cap = models.CharField(
        max_length=255,
        verbose_name=_("Kurslar kichik sarlavhasi")
    )
    courses_title = models.CharField(
        max_length=255,
        verbose_name=_("Kurslar sarlavhasi")
    )
    news2_cap = models.CharField(
        max_length=255,
        verbose_name=_("Ikkinchi yangiliklar kichik sarlavhasi")
    )
    news2_title = models.CharField(
        max_length=255,
        verbose_name=_("Ikkinchi yangiliklar sarlavhasi")
    )
    liders_cap = models.CharField(
        max_length=255,
        verbose_name=_("Liderlar kichik sarlavhasi")
    )
    liders_title = models.CharField(
        max_length=255,
        verbose_name=_("Liderlar sarlavhasi")
    )
    faq_cap = models.CharField(
        max_length=255,
        verbose_name=_("FAQ kichik sarlavhasi")
    )
    faq_title = models.CharField(
        max_length=255,
        verbose_name=_("FAQ sarlavhasi")
    )
    partners_cap = models.CharField(
        max_length=255,
        verbose_name=_("Hamkorlar kichik sarlavhasi")
    )
    partners_title = models.CharField(
        max_length=255,
        verbose_name=_("Hamkorlar sarlavhasi")
    )

    class Meta:
        verbose_name = _("Sarlavhalar")
        verbose_name_plural = _("Sarlavhalar")

    def __str__(self):
        return self.news_title

class HomeCourses(models.Model):
    cap_title = models.CharField(
        max_length=255,
        verbose_name=_("Kichik Sarlavha")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    body = models.TextField(
        verbose_name=_("Matn")
    )
    image = models.ImageField(
        upload_to='courses_images/',
        verbose_name=_("Rasm")
    )
    hover_image = models.ImageField(
        upload_to='courses_images/',
        verbose_name=_("Hover rasmi"),
    )

    class Meta:
        verbose_name = _("3. Kurslar")
        verbose_name_plural = _("3. Kurslar")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})

class HomeLeader(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Ism familiya")
    )
    image = models.ImageField(
        upload_to='leaders_images/',
        verbose_name=_("Rasm")
    )
    position = models.CharField(
        max_length=255,
        verbose_name=_("Lavozim")
    )
    facebook_url = models.CharField(
        max_length=255,
        verbose_name=_("Facebook Havolasi"),
        default="#"
    )
    telegram_url = models.CharField(
        max_length=255,
        verbose_name=_("Telegram Havolasi"),
        default="#"
    )

    class Meta:
        verbose_name = _("4. Rahbarlar")
        verbose_name_plural = _("4. Rahbarlar")

    def __str__(self):
        return f"{self.title} - {self.position}"

class FaqTitle(models.Model):
    cap_title = models.CharField(
        max_length=255,
        verbose_name=_("Kichik Sarlavha")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    image = models.ImageField(
        upload_to='faq_titles/',
        verbose_name=_("Rasm")
    )

    class Meta:
        verbose_name = _("5. FAQ Sarlavha")
        verbose_name_plural = _("5. FAQ Sarlavha")

    def __str__(self):
        return self.title

class Faq(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    body = models.TextField(
        verbose_name=_("Matn")
    )

    class Meta:
        verbose_name = _("5. FAQlar")
        verbose_name_plural = _("5. FAQlar")

    def __str__(self):
        return self.title

class Partner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    image = models.ImageField(
        upload_to='partners/',
        verbose_name=_("Rasm")
    )
    link = models.CharField(
        max_length=255,
        verbose_name=_("Havola")
    )

    class Meta:
        verbose_name = _("6. Hamkorlar")
        verbose_name_plural = _("6. Hamkorlar")

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    cap_title = models.CharField(
        max_length=255,
        verbose_name=_("Kichik Sarlavha")
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Sarlavha")
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Ism")
    )
    phone = models.CharField(
        max_length=255,
        verbose_name=_("Telefon")
    )
    message = models.TextField(
        verbose_name=_("Xabar")
    )
    body = models.TextField(
        verbose_name=_("Tana Matni")
    )
    submit = models.BooleanField(
        default=False,
        verbose_name=_("Yuborish tugmasi")
    )
    iframe = models.TextField(
        verbose_name=_("Iframe google xarita uchun")
    )
    bot_token = models.TextField(
        verbose_name=_("Bot tokeni")
    )

    class Meta:
        verbose_name = _("6. Biz bilan bog'lanish")
        verbose_name_plural = _("6. Biz bilan bog'lanish")

    def __str__(self):
        return f"{self.name} - {self.phone}"

class Message(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Ism")
    )
    phone = models.CharField(
        max_length=255,
        verbose_name=_("Telefon")
    )
    message = models.TextField(
        verbose_name=_("Xabar")
    )
    is_view = models.BooleanField(
        default=False,
        verbose_name=_("Ko'rilganmi?")
    )

    class Meta:
        verbose_name = _("7. Xabarlar")
        verbose_name_plural = _("7. Xabarlar")

    def __str__(self):
        return f"{self.name} - {self.phone}"
