from django import forms

class ExampleForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()



