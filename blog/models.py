from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_on = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
