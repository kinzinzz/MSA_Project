from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_email

class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, 
                              blank=False, 
                              unique=True,
                              validators=[validate_email])
    
    userName = models.CharField(max_length=50,
                                 blank=False, 
                                 unique=True)
    
    def __str__(self):
        return self.userName