from django.contrib import admin

from schools.models import School, Subject, ClassRoom, Lecture

admin.site.register(School)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Lecture)
