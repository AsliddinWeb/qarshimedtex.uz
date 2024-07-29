from django.shortcuts import get_object_or_404, redirect

from TEXNIKUM.views import base_view

from news_app.models import News, NewsDetailText
from settings_app.models import MoreTitles, TelegramBotSettings

from .models import *
from .utils import send_message


def get_latest_single_instance(model):
    return model.objects.last()

def get_filtered_news(is_elon, limit=9):
    return News.objects.filter(is_elon=is_elon)[:limit]

@base_view(template_name='home.html')
def home_page(request, context):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        send_text = (f"✅ <b>Yangi xabar:</b>\n\n"
                     f"🙂<b>Ism: </b>{name}\n"
                     f"📞 <b>Telefon raqami: </b>{phone}\n"
                     f"🔖 <b>Xabar: </b>{message}")

        telegram_bot = get_latest_single_instance(TelegramBotSettings)
        if telegram_bot:
            send_message(
                token=telegram_bot.token,
                chat_id=telegram_bot.chat_id,
                text=send_text
            )

        new_message = Message(name=name, phone=phone, message=message)
        new_message.save()

        return redirect('home_page')

    context.update({
        'sliders': Slider.objects.order_by('-created_at'),
        'home_about': get_latest_single_instance(HomeAbout),
        'titles': get_latest_single_instance(HomeTitles),
        'news': get_filtered_news(is_elon=False),
        'news2': get_filtered_news(is_elon=True),
        'news_detail_text': get_latest_single_instance(NewsDetailText),
        'home_courses': HomeCourses.objects.all(),
        'faq_title': get_latest_single_instance(FaqTitle),
        'faqs': Faq.objects.all(),
        'partners': Partner.objects.all(),
        'contact_us': get_latest_single_instance(ContactUs),
        'liders': HomeLeader.objects.all()[:3],
    })

    return context

@base_view(template_name='courses/detail.html')
def course_detail(request, context, pk):
    course_item = get_object_or_404(HomeCourses, pk=pk)
    more_titles = get_latest_single_instance(MoreTitles)

    context['course_item'] = course_item
    context['more_titles'] = more_titles
    return context
