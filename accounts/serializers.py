from rest_framework import serializers, validators
from .models import CustomUser, KavProf
from django.contrib.auth import authenticate


# User Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True

            },
            'email': {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        CustomUser.objects.all(), "A user with this Email already exists !"
                    )
                ]
            }
        }

    def create(self, validated_data):
        return CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Username or Password")


class KavprofSerializer(serializers.ModelSerializer):
    class Meta:
        model = KavProf
        fields = (
            'first_name',
            'last_name',
            'usertype',
            'experience',
            'location',
            'birth_date'
        )
