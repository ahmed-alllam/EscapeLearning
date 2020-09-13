from rest_framework import generics, authentication, permissions

from students import serializers
from students.permissions import IsStudent


class RegisterStudentView(generics.CreateAPIView):
    serializer_class = serializers.StudentSerializer


class ManageStudentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.StudentSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsStudent)

    def get_object(self):
        return self.request.user.student
