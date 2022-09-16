from re import T
from django.db import models
from PIL import Image

# Create your models here.

class User(models.Model):
    
    user_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12) 

 
 
class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length= 255,default='default jaipur',)

    def __str__(self):
        return f'{self.user.user_name} User_profile'

 
    