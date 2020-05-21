from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('short_name', 'cource', 'level',
                  # 'start_date', 'payment_date',
                  # 'next_payment_date',
                  'teacher')