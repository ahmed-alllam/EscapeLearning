from django.contrib.auth.models import User
from django.db import models

from students.models import Student


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent')
    profile_photo = models.ImageField(null=True)
    children = models.ManyToManyField(Student, related_name='parents')
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
