from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
  site = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  # phone = models.PositiveIntegerField
  # email = models.EmailField
  # hours = models.DurationField
  # is_open = models.BooleanField(default=False)
  info = models.TextField()
  last_updated = models.DateTimeField(auto_now=True)
  # site_tags = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.site
    
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk}) 
