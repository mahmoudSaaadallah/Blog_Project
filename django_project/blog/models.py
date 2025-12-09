from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # This function returns the url to access a particular blog post
    # After creating a new post we have to tell the Django what is the next distnation so we have to override the success_url or implement get_absolute_url in the Post mode.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


