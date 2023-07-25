from django.db import models

class Question(models.Model):
    question_text = models.TextField(blank=True)
    question_complete = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
        return f'/question/{self.pk}'
    
class Choice(models.Model) :
    choice = models.CharField(max_length=20, blank=True)
    answer = models.BooleanField(default=False, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.question.question_text}의 선택지 -> {self.choice}'