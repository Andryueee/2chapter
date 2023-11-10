from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from .models import Profile



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


from django.views.generic.detail import DetailView
def ShowProfilePageView(request):
    return render(request, 'main/user_profile.html')



def create(request):
    form = ArticlesForm()
    data = {
        'form': form
    }
    return render(request, 'main/create.html')
