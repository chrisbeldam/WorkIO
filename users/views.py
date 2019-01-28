from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserReigsterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserReigsterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created form {username}!")
            return redirect('index')

    else:
        form = UserReigsterForm()
    return render(request, 'users/register.html', {'form': form})
