from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_property = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_PRICE = [
        ('fixed', 'Fixed'),
        ('negotiable', 'Negotiable'),
        ('not_fixed', 'Not fixed')
    ]
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default="Description")
    dateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_PRICE, default='fixed')
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.category} - {self.dateTime}'
