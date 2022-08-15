from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.views import Token
from rest_framework.validators import UniqueValidator
from user_app .models import Profile

posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name','second_name','location')



class UserSerializer(serializers.ModelSerializer):

    profile = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ("username", "password","password2","email","profile")
        extra_kwargs = {
        "password": {"write_only": True},
        "password2" : {"write_only": True}

        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'emal': 'User with this email already exists'})

        user = User(**validated_data)
        user.set_password(password)
        user.save()


        Token.objects.create(user=user)
        return user
