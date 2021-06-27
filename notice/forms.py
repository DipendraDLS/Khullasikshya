from django import forms
from .models import Notice


class AdminNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('notice_title', 'notice_content', 'notice_url',)

        widgets = {'notice_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notice Title'}),
                   'notice_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notice Content'}),
                   'notice_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notice Url'}),

                   }
