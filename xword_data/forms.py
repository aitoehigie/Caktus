from django import forms

class WordForm(forms.Form):
    answer = forms.CharField(label='Enter guess:', max_length=100, required=True)