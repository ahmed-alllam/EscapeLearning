from django.contrib.auth.models import User
from rest_framework import serializers

from classrooms.models import School
from core.serializers import UserSerializer
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('user', 'profile_photo', 'name', 'subject', 'school', 'school_code')
        model = Teacher
        extra_kwargs = {
            'school_code': {'write_only': True}
        }

    def to_representation(self, instance):
        teacher = super().to_representation(instance)

        teacher['subject'] = teacher.get('subject').name
        teacher['school'] = teacher.get('subject').school.name

        return teacher

    def validate(self, attrs):
        if not (school := School.objects.filter(name__i=attrs['school'])):
            raise serializers.ValidationError("Invalid School Name")

        if school.teachers_code != attrs['school_code']:
            raise serializers.ValidationError("Invalid School Code")

        if school.subjects.all().filter(name__i=attrs['subject']):
            raise serializers.ValidationError("Invalid Subject")

        return attrs

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(**user_data)
        user.set_password(user.password)
        user.save()

        school = School.objects.get(name__i=validated_data.pop('school'))
        subject = school.subjects.all().get(name__i=validated_data.pop('subject'))

        return Teacher.objects.create(user=user, subject=subject, **validated_data)
