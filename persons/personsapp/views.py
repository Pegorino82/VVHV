from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.db import transaction

from personsapp.models import Person, Document
from personsapp.forms import PersonModelForm, DocumentModelForm


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'personsapp/create.html'
    success_url = reverse_lazy('personsapp:list_view')
    extra_context = {'title': 'Create'}

    formset_model = Document
    formset_form = DocumentModelForm

    def get_context_data(self, **kwargs):
        document_formset = inlineformset_factory(self.model, self.formset_model, self.formset_form)
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            formset = document_formset(self.request.POST)
        else:
            formset = document_formset()
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super(PersonCreateView, self).form_valid(form)


class PersonListView(ListView):
    model = Person
    template_name = 'personsapp/index.html'
    paginate_by = 3
    extra_context = {'title': 'List'}


class PersonDetailView(DetailView):
    model = Person
    template_name = 'personsapp/detail.html'
    extra_context = {'title': 'Detail'}


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'personsapp/update.html'
    form_class = PersonModelForm
    success_url = reverse_lazy('personsapp:list_view')
    extra_context = {'title': 'Update'}

    formset_model = Document
    formset_form = DocumentModelForm

    def get_context_data(self, **kwargs):
        document_formset = inlineformset_factory(self.model, self.formset_model, self.formset_form)
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            formset = document_formset(self.request.POST, instance=self.object)
        else:
            formset = document_formset(instance=self.object)
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super(PersonUpdateView, self).form_valid(form)
