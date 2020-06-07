from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView, Response
from .serializers import UserSerializer, JWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action != 'create':
            self.permission_classes = (permissions.IsAuthenticated,)

        return super(UserViewSet, self).get_permissions()


class AccountLoginAPIView(TokenObtainPairView):
    serializer_class = JWTSerializer


class UserActivity(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        return Response({'user_id': user_id, 'last_login': user.last_login, 'last_visit': user.last_visit})
