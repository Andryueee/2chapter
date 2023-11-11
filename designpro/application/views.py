from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class ApplicationDetailView(DetailView):
    model = Articles
    template_name = 'application/details_view.html'
    context_object_name = 'article'

class ApplicationUpdateView(UpdateView):
    model = Articles
    template_name = 'application/create.html'

    form_class = ArticlesForm


class ApplicationDeleteView(DeleteView):
    model = Articles
    success_url = '/application/'
    template_name = 'application/application-delete.html'




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