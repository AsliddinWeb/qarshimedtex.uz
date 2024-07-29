from django.shortcuts import render
from functools import wraps

from navbar_app.models import OneNavbar, TwoNavbar, ThreeNavbar
from settings_app.models import *

def base_view(template_name='base.html'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            seo_settings = SeoSettings.objects.last()
            # Navbar
            one_navbars = OneNavbar.objects.all()
            two_navbars = TwoNavbar.objects.all()
            three_navbars = ThreeNavbar.objects.all()

            # Header
            header = HeaderSettings.objects.last()
            social_networks = SocialSettings.objects.all()

            # Footer
            footer = FooterSettings.objects.last()
            footer_link_categories = FooterLinkCategory.objects.all()
            footer_links = FooterLink.objects.all()
            contact_info = ContactInfo.objects.last()

            more_titles = MoreTitles.objects.last()


            context = {
                # Seo
                'seo_settings': seo_settings,
                # Navbar
                'one_navbars': one_navbars,
                'two_navbars': two_navbars,
                'three_navbars': three_navbars,
                # Social
                'social_networks': social_networks,
                # Footer
                'footer': footer,
                'footer_link_categories': footer_link_categories,
                'footer_links': footer_links,
                'contact_info': contact_info,

                # Header
                'header': header,
                'more_titles': more_titles,
            }

            response = view_func(request, context, *args, **kwargs)

            if isinstance(response, dict):
                context.update(response)
                return render(request, template_name, context)
            return response

        return _wrapped_view

    return decorator

def not_found(request, exception):
    error_texts = ErrorTexts.objects.last()
    more_titles = MoreTitles.objects.last()

    ctx = {
        'error_texts': error_texts,
        'more_titles': more_titles,
    }
    return render(request, 'errors/404.html', status=404, context=ctx)

def server_error(request):
    error_texts = ErrorTexts.objects.last()
    more_titles = MoreTitles.objects.last()

    ctx = {
        'error_texts': error_texts,
        'more_titles': more_titles,
    }

    return render(request, 'errors/500.html', status=500, context=ctx)