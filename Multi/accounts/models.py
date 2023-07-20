from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기
from django.core.validators import RegexValidator

class User(AbstractUser):
    old = models.IntegerField(default=0)
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 11, unique = True)
    address = models.CharField(max_length=50)
