from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'pk': self.id})

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    # add user_id FK column
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # create a M:M relationship with Review
    reviews = models.ManyToManyField(Review)
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})