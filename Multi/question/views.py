from django.shortcuts import render
from django.views.generic import ListView
from .models import Question

class QuestionList(ListView):
    model = Question
    template_name='questionlist.html'
