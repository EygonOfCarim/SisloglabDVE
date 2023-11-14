from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        self.fields['is_staff'].required = False
        self.fields['is_active'].required = False
        self.fields['is_superuser'].required = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'is_active', 'email', 'is_staff', 'is_superuser']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'return lettersOnly(event)'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'return capitalize(event,this.id)', 'onkeypress': 'return lettersOnly(event)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'is_staff': forms.CheckboxInput(attrs={}),
            'is_active': forms.CheckboxInput(attrs={}),
            'is_superuser': forms.CheckboxInput(attrs={}),
        }
