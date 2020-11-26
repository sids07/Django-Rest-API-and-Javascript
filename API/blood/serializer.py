from rest_framework.fields import ListField

from .models import UserInfo, Disease
from rest_framework import serializers


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'dis_name']


class UserInfoSerializer(serializers.ModelSerializer):
    blood_group = serializers.CharField()
    name = serializers.CharField()
    image = serializers.ImageField()
    address = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=128)
    age = serializers.IntegerField()
    gender = serializers.CharField()

    disease = DiseaseSerializer(many=True)

    class Meta:
        model = UserInfo
        fields = ['user_id', 'blood_group', 'name', 'image', 'address', 'phone', 'age', 'gender', 'disease']
