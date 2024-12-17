from django import forms

class addTask(forms.Form):
    nameFirst = forms.CharField(label='nameFirst', max_length=20)
    description = forms.CharField(label='description', max_length=20)