from rest_framework import generics, authentication, permissions

from teachers import serializers
from teachers.permissions import IsTeacher


class RegisterTeacherView(generics.CreateAPIView):
    serializer_class = serializers.TeacherSerializer


class ManageTeacherView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TeacherSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsTeacher)

    def get_object(self):
        return self.request.user.teacher
