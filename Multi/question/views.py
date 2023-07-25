from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Question, Choice
from django.contrib import messages

class QuestionList(ListView):
    model = Question     
    
class QuestionDetail(DetailView):
    model = Question

def complete(request, pk):
    choices = get_object_or_404(Choice, pk=pk)
    question = Question.objects.get(id=choices.question.pk)
    if(choices.answer == False and question.question_complete == False):
        choices.answer = True
        question.question_complete=True
        choices.save()
        question.save()
        return redirect('/question')
    elif(choices.answer == True) :
        choices.answer = False
        question.question_complete=False
        choices.save()
        question.save()
        return redirect('/question')
    else:
        choices.save()
        question.save()
        return redirect(question.get_absolute_url())