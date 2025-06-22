from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
