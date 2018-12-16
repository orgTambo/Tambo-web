from django import forms

class LoginForm(forms.Form):
    """Users form for login in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
