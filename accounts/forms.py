from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite a Senha'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirme sua Senha'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'phone_number', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Digite seu Nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Digite seu Sobrenome'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Digite seu Telefone'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
