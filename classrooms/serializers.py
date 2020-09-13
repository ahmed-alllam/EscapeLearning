from rest_framework import serializers

from classrooms.models import ClassRoom, School, Lecture


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('slug', 'name', 'image')
        model = School


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('slug', 'name')
        model = ClassRoom


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('slug', 'name', 'video_url', 'timestamp')
        model = Lecture
