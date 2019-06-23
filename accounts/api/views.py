from accounts.api.serializers import UserSerializer
from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


