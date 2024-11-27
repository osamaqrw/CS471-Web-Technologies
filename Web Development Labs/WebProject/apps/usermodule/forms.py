from django.contrib.auth.models import User
from django import forms

class RecoverForm(forms.Form):
    email = forms.EmailField()
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()