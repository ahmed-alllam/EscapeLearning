from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'password')
        model = User
        extra_kwargs = {
            'password': {
                'min_length': 8, 'write_only': True
            }
        }
