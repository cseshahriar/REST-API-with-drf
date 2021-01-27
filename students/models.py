from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=60)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name