from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class UserNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username',)
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Account
        fields = ('user_type', 'user',)