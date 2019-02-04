from django import forms
from personsapp.models import Person, Document


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(PersonModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document_type', 'number', 'issue_date', 'scan')

    def __init__(self, *args, **kwargs):
        super(DocumentModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
