from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
  site = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  lat = models.FloatField()
  lng = models.FloatField()
  info = models.TextField()
  start_time = models.DateTimeField(auto_now=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(blank=True)

  def __str__(self):
    return self.site
    
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk}) 
