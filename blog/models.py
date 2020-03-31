from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# This is the class representing post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #set the date posted to the time that we create a post
    date_posted = models.DateTimeField(default=timezone.now) 
    #if the user create a post and the user is deleted, then the post is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title