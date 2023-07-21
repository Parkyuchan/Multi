from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Choice

class QuestionList(ListView):
    model = Question
    choices = Choice.objects.all() 
     
    
class QuestionDetail(DetailView):
    model = Question
    choices = Choice.objects.all()  
    
class ChoiceList(ListView):
    model = Choice

def complete(request, pk):
    choices = get_object_or_404(Choice, pk=pk)
    choices.answer = True
    choices.save()
    return redirect('/question')