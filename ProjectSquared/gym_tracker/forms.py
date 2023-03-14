from django import forms

class SpSheetForm(forms.Form):
    file = forms.FileField()