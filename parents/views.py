from rest_framework import generics, authentication, permissions

from parents import serializers
from parents.permissions import IsParent


class RegisterParentView(generics.CreateAPIView):
    serializer_class = serializers.ParentSerializer


class ManageParentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ParentSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsParent)

    def get_object(self):
        return self.request.user.parent
