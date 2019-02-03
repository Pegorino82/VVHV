from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy

from personsapp.models import Person
from personsapp.forms import PersonModelForm


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'personsapp/create.html'
    success_url = reverse_lazy('personsapp:list_view')


class PersonListView(ListView):
    model = Person
    template_name = 'personsapp/index.html'
    paginate_by = 3


class PersonDetailView(DetailView):
    model = Person
    template_name = 'personsapp/detail.html'
