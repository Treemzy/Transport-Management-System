from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class MaritalStatus(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class EdQual(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Role(models.Model):
    role = models.CharField(max_length=100, null=True, blank=True, default=None)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role

    def get_absolute_url(self):
        return reverse('TMS-Role')


class User(AbstractUser):
    is_driver = models.BooleanField('Driver', default=False)
    is_passenger = models.BooleanField('Passenger', default=False)
    is_admin = models.BooleanField('Admin', default=False)
    is_superadmin = models.BooleanField('Super Admin', default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    roles = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('congrats')


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    matricNo = models.CharField(max_length=100, null=True, blank=True, default=None)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True, default=None)
    lga = models.CharField(max_length=100, null=True, blank=True, default=None)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    phoneNumber = models.CharField(max_length=100, null=True, blank=True, default=None)
    address = models.TextField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('passenger_register')


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True, default=None)
    lga = models.CharField(max_length=100, null=True, blank=True, default=None)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    edQlf = models.ForeignKey(EdQual, null=True, on_delete=models.SET_NULL)
    carType = models.ForeignKey(CarType, null=True, on_delete=models.SET_NULL)
    maritalStatus = models.ForeignKey(MaritalStatus, null=True, on_delete=models.SET_NULL)
    nok = models.CharField(max_length=100, null=True, blank=True, default=None)
    serialNumber = models.CharField(max_length=100, null=True, blank=True, default=None)
    plateNumber = models.CharField(max_length=100, null=True, blank=True, default=None)
    phoneNumber = models.CharField(max_length=100, null=True, blank=True, default=None)
    address = models.TextField()
    is_active = models.BooleanField('Active', default=False)
    is_car_owner = models.BooleanField('Car Owner', default=False)

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('driver_register')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField('Active', default=False)
    bio = models.CharField(max_length=100, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

