from django.contrib.auth.models import User

from classrooms.models import School
from core.serializers import UserSerializer

from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('user', 'profile_photo', 'name', 'classroom', 'school', 'school_code',
                  'code', 'points', 'rating')
        model = Student
        extra_kwargs = {
            'school_code': {'write_only': True},
            'code': {'read_only': True}
        }

    def to_representation(self, instance):
        teacher = super().to_representation(instance)

        teacher['classroom'] = teacher.get('classroom').name
        teacher['school'] = teacher.get('classroom').school.name

        return teacher

    def validate(self, attrs):
        if not (school := School.objects.filter(name__i=attrs['school'])):
            raise serializers.ValidationError("Invalid School Name")

        if school.students_code != attrs['school_code']:
            raise serializers.ValidationError("Invalid School Code")

        if school.classrooms.all().filter(name__i=attrs['classroom']):
            raise serializers.ValidationError("Invalid Classroom")

        return attrs

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(**user_data)
        user.set_password(user.password)
        user.save()

        school = School.objects.get(name__i=validated_data.pop('school'))
        classroom = school.subjects.all().get(name__i=validated_data.pop('classroom'))

        return Student.objects.create(user=user, classroom=classroom, **validated_data)

