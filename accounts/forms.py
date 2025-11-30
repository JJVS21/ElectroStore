from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BaseRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError("Las contraseñas no coinciden.")
        return p2

class SellerRegisterForm(BaseRegisterForm):
    # campos adicionales si los necesitas
    pass

class ManagerRegisterForm(BaseRegisterForm):
    # campos adicionales si los necesitas
    pass
