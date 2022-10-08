from django import forms
import django_filters
from .models import WorkEvidence
from django_filters import DateTimeFilter, AllValuesFilter,ModelChoiceFilter

class WorkEvidenceFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="start_date",widget= forms.DateTimeInput(attrs={ 'type': 'datetime-local'}),lookup_expr="gte", label="Datum začetka")
    end_date = DateTimeFilter(field_name="end_date",widget=forms.DateTimeInput(attrs={ 'type': 'datetime-local'}),lookup_expr="lte", label="Datum konca")   
    class Meta:
        model = WorkEvidence
        fields = '__all__'
        exclude = ['created_date']