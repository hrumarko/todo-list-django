from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, label='Tasks', widget=forms.TextInput(attrs={
        'class': 'input-task',
        'placeholder': 'Task'
        }))
    description = forms.CharField(max_length=150, widget=forms.Textarea(attrs={
        'class': 'input-description',
        'placeholder': 'Description',
        'rows': 2,
        }))
    date = forms.DateTimeField(required=False,
                               input_formats=['%d/%m/%Y %H:%M'],
                               widget=forms.DateInput(
                                    attrs={
                                        'class': 'time-input',
                                        'placeholder': 'Without date'
                                    }))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(attrs={
            'class': 'reg-input'
        })
        )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'reg-input'
        })
        )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'reg-input'
            })
        )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={
            'class': 'reg-input'
            })
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
