from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True,default = 'Bio Will Appear Here')
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True,default = '../static/images/default.png')
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	

	def __str__(self):
		return self.user

	@property
	def all_comments(self):
		return self.comments.all()

class Image(models.Model):
	
	image_name = models.CharField(max_length = 60, blank = True)
	image_caption = models.CharField(max_length = 60, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	profile = models.ForeignKey(User)
	user_profile = models.ForeignKey(Profile)
	likes = models.ManyToManyField(User,related_name = 'likes', blank = True)
	image = models.ImageField(upload_to = 'images/', blank = True)