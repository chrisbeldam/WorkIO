from django.shortcuts import render
from django.http import HttpResponse

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
    form = ContractCreateForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse('Your form has been successfully submitted')
        else:
            return HttpResponse('The form you submitted was invalid, please try again')
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'jobs/create.html', context)

# def edit_a_contract(request):
#     pass

# def delete_a_contract(request):
#     pass

def results(request):
    """ Returns any search results for jobs """
    page_title = "Search Results"
    context = {
        'page_title': page_title
    }
    return render(request, 'jobs/results.html', context)
