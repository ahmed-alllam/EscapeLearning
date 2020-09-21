from django.contrib.auth.models import User
from django.db import models

from schools.models import Subject


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    profile_photo = models.ImageField(null=True)
    name = models.CharField(max_length=1024)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
