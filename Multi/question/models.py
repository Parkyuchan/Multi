from django.db import models

class Question(models.Model):
    question_text = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model) :
    choice = models.CharField(max_length=20, blank=True)
    answer = models.BooleanField(default=False, blank=True)
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.question_text}의 선택지 -> {self.choice}'