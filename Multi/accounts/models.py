from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기
from django.core.validators import RegexValidator
from django.conf import settings
    
class User(AbstractUser):
    old = models.IntegerField(default=0)
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 11, unique = True)
    address = models.CharField(max_length=50)
    volunteer = models.BooleanField(default=False, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def __str__(self):
        if self.volunteer == True:
            return f'자원봉사자 {self.username}님'
        else:
            return f'교통약자 {self.username}님'