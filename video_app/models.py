from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Group(models.Model):
    group_title = models.CharField(max_length=255)

    def __str__(self):
        return self.group_title

class Video(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=50)
    video_url = models.URLField(blank=True) 
    video_file = models.FileField(upload_to='media/', blank=True)

    

    def __str__(self):
        
        return self.video_title
        
class Comment(models.Model):
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

