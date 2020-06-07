from rest_framework import serializers
from .models import User
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt import serializers as JWTserializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class JWTSerializer(JWTserializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        update_last_login(None, self.user)
        return validated_data
