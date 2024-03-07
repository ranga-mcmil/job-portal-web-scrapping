from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.forms import ClearableFileInput
from portal.models import Category



class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'form-control',
        'placeholder': 'Username',
        'id': 'search-input01'
       }
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'form-control', 'placeholder': 'Password', 'id': 'search-input01'}
    )



class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'search-input01',
            'placeholder': 'Username'
        }
    ))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'name': 'category',
            'id': 'search-input01',
            'placeholder': 'Category'
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'id': 'search-input01',
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'id': 'search-input01',
            'placeholder': 'Confirm Password'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'category')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')



class UserUpdateForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'name': 'category',
        }
    ))
    
    class Meta:
        model = User
        fields = ('category', )

