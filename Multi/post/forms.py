from django import forms
from .models import Post

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'started_date', 'started_time', 'arrive_place']
        widgets = {
            'started_date' : DateInput(),
            'started_time' : TimeInput()
        }