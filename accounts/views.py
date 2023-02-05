from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import UserSecondarySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class BlacklistRefreshView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondarySerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)
