from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class UserSecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',)

        def update(self, instance, validated_data):
            first_name = validated_data.pop('first_name', None)
            last_name = validated_data.pop('last_name', None)
            email = validated_data.pop('email', None)
            return super().update(instance, validated_data)
