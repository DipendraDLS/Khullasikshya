from login_signup.models import User
from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

    class Meta:
        model = User
        fields = {'image'}


class AddNameForm(forms.Form):
    """Image upload form."""
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = {'first_name', 'last_name'}
