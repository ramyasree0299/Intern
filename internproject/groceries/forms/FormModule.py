from django import forms
from groceries.models import *
class AddItem(forms.ModelForm):
    class Meta:
        model = grocery_items
        fields= "__all__"


class Login(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input','placeholder':"Enter username"}),
        max_length=50,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': "Enter username"}),
        max_length=50,
        required=True
    )
