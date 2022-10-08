from django import forms
from .models import WorkEvidence, Worker
from .widgets import DatePicker, DateTimePickerInput

class WorkerForm(forms.ModelForm):
    first_name = forms.CharField(label='Ime', max_length=100)
    last_name = forms.CharField(label='Priimek', max_length=100)
    card_id = forms.CharField(label='Številka kartice', max_length=100)
    date_of_birth = forms.DateField(label='Datum rojstva',widget=forms.DateInput(attrs={ 'type': 'date'}))
    class Meta:
        model = Worker
        fields = ('first_name', 'last_name','date_of_birth','card_id')
        widgets = {
            'date_of_birth': DatePicker()
        }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = WorkEvidence
        fields = ('start_date','end_date','worker')
        widgets = {
            'start_date': DateTimePickerInput(),
            'end_date': DateTimePickerInput()
        }