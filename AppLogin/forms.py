from django import forms
from django.forms import widgets
from .models import User, StudnetProfile, TeacherProfile
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    choices = (
        ('', "Account Type"),
        ('1', 'Student'),
        ('2','Teacher'),
    )
    type = forms.ChoiceField(label='', choices=choices, required=True)
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={
        'placeholder':'Email Address',
    }))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Type your password'
    }))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Type your password again'
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'type', 'password1', 'password2']
        labels = {
            'first_name': '',
            'last_name':'',
            'email': '',
            'password1': '',
            'password2': '',
        }
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'placeholder':'First Name',
                'autofocus':True
            }),
            'last_name': widgets.TextInput(attrs={
                'placeholder':'Last Name'
            }),

        }

class StudentProfileEdit(forms.ModelForm):
    class Meta:
        model = StudnetProfile
        exclude = ['user']
class TeacherProfileEdit(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ['user']