from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from personsapp.models import Person
from personsapp.forms import PersonModelForm


class PersonListView(ListView):
    model = Person
    template_name = 'personsapp/index.html'
    paginate_by = 3


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'personsapp/create.html'
    success_url = reverse_lazy('personsapp:list_view')
