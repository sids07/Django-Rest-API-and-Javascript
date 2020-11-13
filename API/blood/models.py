from django.db import models
from django.contrib.auth import get_user_model


class Blood(models.Model):
    group = models.CharField(max_length=10, null=True)


class Disease(models.Model):
    dis_name = models.CharField(max_length=20, null=True)


User = get_user_model()


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='info', blank=True, default='image/blood.jpg')
    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=128, null=True)
    age = models.IntegerField(null=True)
    blood = models.ForeignKey(Blood, on_delete=models.SET_NULL, null=True)
    BG = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    blood_group = models.CharField(max_length=10, choices=BG, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=128, null=True)
    disease = models.ManyToManyField(Disease)
