from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Review(models.Model) :
    rating = models.IntegerField() 
    comment = models.TextField()
    user = models.CharField(max_length=100)