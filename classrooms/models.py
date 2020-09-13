from django.db import models


class School(models.Model):
    slug = models.SlugField(unique=True, max_length=255, db_index=True,
                            allow_unicode=True, editable=False)
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=True)
    teachers_code = models.IntegerField()
    students_code = models.IntegerField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    school = models.ManyToManyField(School, related_name='subjects')
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('school', 'name')


class ClassRoom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    slug = models.SlugField(unique=True, max_length=255, db_index=True,
                            allow_unicode=True, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='lectures')
    slug = models.SlugField(unique=True, max_length=255, db_index=True,
                            allow_unicode=True, editable=False)
    name = models.CharField(max_length=255)
    video_url = models.URLField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
