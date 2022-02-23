from dataclasses import field
from .models import Dog, ToDo
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import serializers

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'age']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = ToDo
        fields = ['item']

        from rest_framework import serializers
