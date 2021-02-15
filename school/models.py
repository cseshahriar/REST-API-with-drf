from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Profile(models.Model):
    age = models.PositiveBigIntegerField(null=True)
    # one to one
    student = models.OneToOneField(Student, on_delete=models.CASCADE,
                    related_name='profile_student')

    def __str__(self):
        return self.name

@receiver(post_save, sender=Student)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class School(models.Model):
    name = models.CharField(max_length=60)
   
    def __str__(self):
        return self.name


class Klass(models.Model):
    name = models.CharField(max_length=60)
    # m2o
    school = models.ForeignKey(School, on_delete=models.CASCADE, 
                                related_name='klass_school')
    # m2m
    student = models.ManyToManyField(Student, related_name='klass_student')
