from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
def application_home(request):
    application = Articles.objects.all()
    return  render(request, 'application/application_home.html', {'application': application})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'application/create.html', data)