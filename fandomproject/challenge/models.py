from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

## 준오님
# class Video(models.Model):
#     title = models.CharField(max_length=20)
#     video = models.FileField(upload_to="video/%y")

#     def __str__(self):
#         return self.title

class Video(models.Model):
    # title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='challenge_upload/', default=datetime.now)
    
class Ref_Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    singer = models.CharField(max_length=10, default=None)
    video_file = models.FileField(upload_to='ref_video/', default=datetime.now)
    
class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    score = models.IntegerField()
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)