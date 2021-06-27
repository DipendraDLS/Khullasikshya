from django import forms
from .models import Blog


class AdminBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content', 'blog_image')

        widgets = {'blog_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                   'blog_content': forms.Textarea(
                       attrs={'class': 'form-control', 'placeholder': 'Blog Content'}),
                   }
