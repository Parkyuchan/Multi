from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    choice1 = models.CharField(max_length=20, blank=True)
    choice2 = models.CharField(max_length=20, blank=True)
    choice3 = models.CharField(max_length=20, blank=True)
    choice4 = models.CharField(max_length=20, blank=True)
    answer = models.IntegerField(default=0, blank=True)
    
    def __str__(self):
        return self.question_text