import requests
from django.http import JsonResponse
from django.shortcuts import render


def ajax_with_vanilla_javascript(request):
    return render(request, 'ajax_vanilla_js.html')


def ajax_with_jquery(request):
    return render(request, 'ajax_jquery.html')


def ajax_with_django_view(request):
    return render(request, 'ajax_django_view.html')


def get_movies_response(request):
    search_query = request.GET.get('query')
    # Ganti API Key dengan key pribadi
    url = f"http://omdbapi.com/?apikey=449e4a6b&s={search_query}"
    response = requests.get(url=url)
    return JsonResponse(data=response.json())
