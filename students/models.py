from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from schools.models import ClassRoom


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    v = models.ImageField(null=True)
    classroom = models.ForeignKey(ClassRoom, null=True, related_name='students', on_delete=models.SET_NULL)
    points = models.IntegerField()
    rating = models.SmallIntegerField(validators=[validators.MaxValueValidator(5),
                                                  validators.MinValueValidator(1)])
    name = models.CharField(max_length=1024)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
