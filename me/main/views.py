from django.shortcuts import render, redirect

from .forms import FactForms
from .models import Facts


def index(request):
    return render(request, 'main/index.html')

def about(request):
    facts = Facts.objects.all()
    return render(request, 'main/about.html', {'facts': facts})

def add_fact(request):
    error = ''
    if request.method == 'POST':
        form = FactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Факт заполнен неверно'

    form = FactForms()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_fact.html', context)