from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(
        Author, related_name='books',on_delete=models.CASCADE)