from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'publicate_date', 'isbn']

class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = ApiUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = ApiUser
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}