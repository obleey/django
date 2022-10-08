from django import forms
   
class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime-local'

class DatePicker(forms.DateTimeInput):
        input_type = 'date'