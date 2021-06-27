from django import forms
from .models import ProgrammingLanguage


class ProgrammingForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ('p_title', 'p_code', 'p_link', 'p_language')

        widgets = {'p_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programming Title'}),
                   'p_code': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Programming Code'}),
                   'p_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programming Youtube Link'}),

                   }
