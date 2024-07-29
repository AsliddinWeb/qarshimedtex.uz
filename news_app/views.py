from django.shortcuts import get_object_or_404

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from TEXNIKUM.views import base_view
from settings_app.models import MoreTitles

from .models import News, NewsDetailText, Category

def get_latest_single_instance(model):
    return model.objects.last()

def paginate_queryset(request, queryset, per_page=9):
    paginator = Paginator(queryset, per_page)
    page = request.GET.get('page')

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset

@base_view(template_name='news/detail.html')
def news_detail(request, context, pk):
    news_item = get_object_or_404(News, pk=pk)

    context.update({
        'news_item': news_item,
        'related_news': News.objects.exclude(pk=pk)[:2],
        'news_detail_text': get_latest_single_instance(NewsDetailText),
        'more_titles': get_latest_single_instance(MoreTitles),
        'news_categories': Category.objects.all(),
    })

    return context

@base_view(template_name='news/all_news.html')
def all_news(request, context):
    news_list = News.objects.all()

    context.update({
        'news_detail_text': get_latest_single_instance(NewsDetailText),
        'more_titles': get_latest_single_instance(MoreTitles),
        'all_news': paginate_queryset(request, news_list),
    })

    return context

@base_view(template_name='news/all_news.html')
def category_news(request, context, category_pk):
    news_list = News.objects.filter(category__pk=category_pk)

    context.update({
        'news_detail_text': get_latest_single_instance(NewsDetailText),
        'more_titles': get_latest_single_instance(MoreTitles),
        'all_news': paginate_queryset(request, news_list),
    })

    return context

@base_view(template_name='news/all_news.html')
def news_search(request, context):
    query = request.GET.get('q', '')

    if query:
        news_list = News.objects.filter(
            Q(title__icontains=query) |
            Q(title_uz__icontains=query) |
            Q(title_ru__icontains=query) |
            Q(title_en__icontains=query) |
            Q(body__icontains=query) |
            Q(body_uz__icontains=query) |
            Q(body_ru__icontains=query) |
            Q(body_en__icontains=query)
        )
    else:
        news_list = News.objects.all()

    context.update({
        'news_detail_text': get_latest_single_instance(NewsDetailText),
        'more_titles': get_latest_single_instance(MoreTitles),
        'all_news': paginate_queryset(request, news_list),
        'query': query,
    })

    return context
