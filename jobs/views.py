from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'jobs/index.html', context)

def results(request):
    page_title = "Search Results"
    context = {
        'page_title': page_title
        }
    return render (request, 'jobs/results.html', context)
