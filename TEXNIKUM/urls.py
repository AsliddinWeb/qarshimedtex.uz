from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler404, handler500

# Error pages
from TEXNIKUM.views import not_found, server_error

# Admin UI
admin.site.site_title = "QarshiMedTex.Uz"
admin.site.site_header = "Admin panel"
admin.site.index_title = "Dashboard"

handler404 = not_found
handler500 = server_error

urlpatterns = [
    path('admin/', admin.site.urls),

    # Lang
    path('i18n/', include('django.conf.urls.i18n')),

    # Ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    # Home
    path('', include('home_app.urls')),

    # News
    path('news/', include('news_app.urls')),

    # Pages
    path('page/', include('page_app.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
