from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True,default = 'Bio Will Appear Here')
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True,default = '../static/images/default.png')
	user = models.ForeignKey(User, on_delete = models.CASCADE)