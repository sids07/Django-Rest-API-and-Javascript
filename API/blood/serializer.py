from .models import UserInfo
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['user_id', 'image', 'name', 'phone', 'age', 'blood_group', 'gender', 'address']