from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


from codes.models import Code
class CodeForm(forms.ModelForm):
    number=forms.CharField(label='Code', help_text='Enter SMS verification code')
    class Meta:
        model=Code 
        fields = ('number',)

    