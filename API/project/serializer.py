from rest_framework import serializers
from django.contrib.auth import authenticate

from rest_framework.fields import ListField

class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):# convert list to string
        return ",".join([str(element) for element in obj])
    # [a,b,c] == 'a,b,c'


class Signup(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=True)

    blood = serializers.CharField()
    # image = serializers.ImageField()
    address = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=128)
    age = serializers.IntegerField()
    gender = serializers.CharField()

    disease = StringArrayField()

    def validate(self, data):
        password = data["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError('Password donot match')
        return data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField()

    def validate(self, data):

        username = data["username"]
        password = data["password"]

        if username and password:

            user = authenticate(username=username, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to login with given credentials")
        else:
            raise exceptions.ValidationError("Must provide username and password")
        return data
