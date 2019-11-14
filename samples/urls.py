from django.urls import path

from samples.views import ajax_with_vanilla_javascript, ajax_with_jquery, ajax_with_django_view, get_movies_response

urlpatterns = [
    path('vanilla-js/', ajax_with_vanilla_javascript, name='vanilla-js'),
    path('jquery/', ajax_with_jquery, name='jquery'),
    path('django-view/', ajax_with_django_view, name='django-view'),
    path('response/', get_movies_response, name='movies-response'),
]
