from django.db import models
from django.utils import timezone # import timezone for date handling

class Blogbpost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)  # auto set to now 
    author = models.CharField(max_length=100,default='pramod')
    def __str__(self):
        return self.title

# Create your models here.
