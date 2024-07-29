from django.urls import path

from .views import home_page, course_detail


urlpatterns = [
    path('', home_page, name='home_page'),

    # Courses
    path('course/<int:pk>/', course_detail, name='course_detail'),
]