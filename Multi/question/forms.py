from django import forms
from .models import Question


class QuesForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['answer']
  
class GeeksForm(forms.Form):
    geeks_field = forms.BooleanField( )