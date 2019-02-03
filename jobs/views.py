from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContractCreateForm
from jobs.models import Contract
import datetime

# class ContractListView(ListView):
#     """ Displays all contracts """
#     template_name = 'jobs/results.html'
#     queryset = Contract.objects.all()

class ContractDetailView(DetailView):
    model = Contract
    page_title = "Detail View"

class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    fields = ['contract_title', 'contract_description', 'contract_location', 'contract_monthly_salary',
              'contract_recruiter','recruiter_email', 'recruiter_telephone','contract_expiry_date', 'author']

class ContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contract
    fields = ['contract_title', 'contract_description', 'contract_location', 'contract_monthly_salary',
              'contract_recruiter','recruiter_email', 'recruiter_telephone','contract_expiry_date', 'author']
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contract
    success_url = '/'
    page_title = "Delete View"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def contract_model_list_view(request):
    search_query = request.GET.get('search')
    queryset = Contract.objects.all()
    if search_query is not None:
        queryset = queryset.filter(
            Q(contract_title__icontains=search_query) | Q(contract_location__icontains=search_query) 
            )
    context = {
        'object_list': queryset,
    }
    template="jobs/results.html"
    return render(request, template, context)

def index(request):
    """ Takes you back to the home page """
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'jobs/index.html', context)

# def create_a_contract(request):
#     """ Creates a contract for the website on submission of the form """
#     page_title = "Create your contract"
#     if request.method == "POST":
#         form = ContractCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/results/')
#         else:
#             return HttpResponse('The form you submitted was invalid, please try again')
#     else:
#         form = ContractCreateForm()
#     context = {
#         'form': form,
#         'page_title': page_title
#     }
#     return render(request, 'jobs/create.html', context)

def edit_a_contract(request):
    """ Allows user to edit their contract once submitted """
    page_title = "Edit your contract"

    pass

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

def contract_creation_email(request):
    """ Sends the user and the admin an email to confirm the job was posted """
    user_email = ""
    admin_email = ""
    email_message = ""
    pass

def check_enhanced_expiry(request):
    """ Checks all of the jobs to see which are enhanced, then if they are expired it unenhances them """
    if Contract.objects.get(featured_contract = True): # grabs whether the contract is enhanced or not
        pass

# def delete_a_contract(request):
#     pass
