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

def my_contract(request):
    return render(request, 'jobs/myjobs.html')

def index(request):
    """ Takes you back to the home page """
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'jobs/index.html', context)


def results(request):
    """ Returns any search results for jobs """
    page_title = "Search Results"
    context = {
        'page_title': page_title
    }
    return render(request, 'jobs/results.html', context)
