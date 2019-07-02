from django import forms

from django.contrib.auth.hashers import make_password
from students.models import Person


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail',
        'maxlength': 250,
        'required': 'required',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'minlength': 8,
        'maxlength': 100,
        'required': 'required'
    }))


    class Meta:
        model = Person
        fields = ['email', 'password']


class Register(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'pattern': '[a-z]{3,}',
        'placeholder': 'First name',
        'required': 'required'
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'pattern': '[a-z]{3,}',
        'placeholder': 'Middle name',
        'required': 'required'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail',
        'maxlength': 250,
        'required': 'required',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'pattern': '(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
        'placeholder': 'New Pass',
        'required': 'required',
    }))
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'pattern': '(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
        'placeholder': 'Confirm Password',
        'required': 'required',
    }))


    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'pattern': '[0-9]{11}',
        'placeholder': 'Phone Number',
        'required': 'required'
    }))

    age = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'pattern': '[0-9]{2}',
        'placeholder': 'Age',
        'required': 'required'
    }))

    # Date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Birth Date',
    #     'required': 'required',
    #     'type': 'date'
    # }), input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%m-%Y'])




    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)

    class Meta:
        model = Person
        fields = ['first_name',
                  'second_name',
                  'email',
                  'password',
                  'Confirm_Password',
                  'phone',
                  'age']
