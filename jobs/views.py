from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import ContractCreateForm

def index(request):
    """ Takes you back to the home page """
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'jobs/index.html', context)

def create_a_contract(request):
    """ Creates a contract for the website on submission of the form """
    page_title = "Create your contract"
    if request.method == "POST":
        form = ContractCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/results/')
        else:
            return HttpResponse('The form you submitted was invalid, please try again')
    else:
        form = ContractCreateForm()
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'jobs/create.html', context)

def home_page_search(request):
    """ Runs the search from the homepage """
    pass

def results(request):
    """ Returns any search results for jobs """
    page_title = "Search Results"
    context = {
        'page_title': page_title
    }
    return render(request, 'jobs/results.html', context)

# def edit_a_contract(request):
#     pass

# def delete_a_contract(request):
#     pass
