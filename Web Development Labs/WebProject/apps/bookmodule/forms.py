from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'edition', 'author', 'coverPage']

    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        })
    )

    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0,
            'step': '0.01'
        })
    )

    edition = forms.IntegerField(
        required=True,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1
        })
    )

    author = forms.CharField(
        max_length=100,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={
            'placeholder': 'Select author'
        })
    )

    coverPage = forms.FileField(
        required=True,
        label="Cover Page",
        widget=forms.ClearableFileInput()
    )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        name = forms.CharField(label='Name', required=True)
        age = forms.IntegerField(label='Age',required=True,)
        address = forms.ModelChoiceField(
            label="Address",
            queryset=Address.objects.all().order_by('city'),
            widget=forms.ChoiceField()
        )

class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'address']
    name = forms.CharField(label='Name', required=True)
    age = forms.IntegerField(label='Age',required=True,)
    address = forms.ModelMultipleChoiceField(
        label="Address",
        queryset=Address2.objects.all().order_by('city'),
        widget=forms.CheckboxSelectMultiple()
    )
