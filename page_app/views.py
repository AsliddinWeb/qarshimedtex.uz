from django.shortcuts import get_object_or_404

from TEXNIKUM.views import base_view
from settings_app.models import MoreTitles

from .models import Page

@base_view(template_name='pages/detail.html')
def page_detail(request, context, slug):
    page = get_object_or_404(Page, slug=slug)
    more_titles = MoreTitles.objects.last()

    context['page'] = page
    context['more_titles'] = more_titles

    return context
