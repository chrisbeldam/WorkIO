from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContractCreateForm

def index(request):
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'jobs/index.html', context)

def create_a_contract(request):
    """ Creates a contract for the website on submission of the form """
    form = ContractCreateForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse('Test')
    context = {
        'form': form
    }
    return render(request, 'jobs/create.html', context)

# def edit_a_contract(request):
#     pass

# def delete_a_contract(request):
#     pass

def results(request):
    page_title = "Search Results"
    context = {
        'page_title': page_title
    }
    return render(request, 'jobs/results.html', context)
