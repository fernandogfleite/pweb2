from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(), max_length=128, label="Senha")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        cleaned_data = self.clean()
        email = cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Um usuário com este email já existe.')

        return email


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Usuário")
    password = forms.CharField(
        widget=forms.PasswordInput(), max_length=128, label="Senha")
