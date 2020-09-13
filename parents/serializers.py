from django.contrib.auth.models import User

from core.serializers import UserSerializer
from parents.models import Parent

from rest_framework import serializers

from students.models import Student


class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('user', 'profile_photo', 'name', 'child_code')
        model = Parent
        extra_kwargs = {
            'child_code': {'write_only': True}
        }

    def validate_child_code(self, value):
        if not Student.objects.filter(code=value):
            raise serializers.ValidationError("Invalid Child Code")

        return value

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(**user_data)
        user.set_password(user.password)
        user.save()

        child = Student.objects.get(code=validated_data.pop('child_code'))

        parent = Parent.objects.create(user=user, **validated_data)
        parent.children.add(child)
        return parent
