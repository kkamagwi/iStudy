from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('surname', 'name', 'group','active' ,'admission_date', 'notes')
