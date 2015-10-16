from django import forms
from django.forms import widgets

from timepiece.crm.models import Business
from timepiece.utils.search import SearchForm

from .models import Document

class AddDocument(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('industry', 'business', 'ata', 'discipline',
            'name', 'description')

    def __init__(self, *args, **kwargs):
        super(AddDocument, self).__init__(*args, **kwargs)
        self.fields['ata'].label = 'ATA'

class EditDocument(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('name', 'description')

class DocumentSearchForm(SearchForm):
    industry = forms.ChoiceField(required=False, label='')
    business = forms.ChoiceField(required=False, label='')
    discipline = forms.ChoiceField(required=False, label='')
    ata = forms.IntegerField(required=False, label='')

    def __init__(self, *args, **kwargs):
        super(DocumentSearchForm, self).__init__(*args, **kwargs)
        self.fields['ata'].widget.attrs['placeholder'] = 'ATA'
        self.fields['industry'].choices = [('', 'Any Industry')] + \
            list(Document.INDUSTRIES)
        businesses = [(b.id, str(b)) for b in Business.objects.filter()]
        self.fields['business'].choices = [('', 'Any Business')] +  businesses
        self.fields['discipline'].choices = [('', 'Any Discipline')] + \
            list(Document.DISCIPLINES)
