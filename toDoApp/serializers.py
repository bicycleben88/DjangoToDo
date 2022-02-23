from dataclasses import field
from .models import ToDo
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import serializers

UserModel = get_user_model()


class ToDoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ToDo
        fields = ['item', 'user']

        
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    todos = ToDoSerializer(many=True, read_only=True)
    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "todos")

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

