from urllib import request

from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import (Passenger,
                      Driver,
                      User,
                      Profile,
                      Gender,
                      EdQual,
                        CarType,
                        MaritalStatus,
                      )
from django.forms.widgets import NumberInput


class PassengerSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Confirm Password"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    other_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    matricNo = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    dob = forms.DateField(widget=NumberInput(attrs={
        'type': "date"

    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    lga = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))

    gender = forms.ModelChoiceField(queryset=Gender.objects.all())

    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))

    address = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text",

    }))

    def __init__(self, *args, **kwargs):
        super(PassengerSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_passenger = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.other_name = self.cleaned_data.get('other_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        passenger = Passenger.objects.create(user=user)
        passenger.matricNo = self.cleaned_data.get('matricNo')
        passenger.dob = self.cleaned_data.get('dob')
        passenger.state = self.cleaned_data.get('state')
        passenger.lga = self.cleaned_data.get('lga')
        passenger.gender = self.cleaned_data.get('gender')
        passenger.phoneNumber = self.cleaned_data.get('phoneNumber')
        passenger.address = self.cleaned_data.get('address')
        passenger.save()
        return user


class DriverSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Confirm Password"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    other_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
    }))
    dob = forms.DateField(widget=NumberInput(attrs={
        'type': "date"

    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    lga = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))

    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    edQlf = forms.ModelChoiceField(queryset=EdQual.objects.all())
    carType = forms.ModelChoiceField(queryset=CarType.objects.all())
    maritalStatus = forms.ModelChoiceField(queryset=MaritalStatus.objects.all())

    nok = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    serialNumber = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
        }))
    plateNumber = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
        }))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
        }))
    is_car_owner = forms.BooleanField(label_suffix = " : ",
          disabled = False,
          required = False,
          widget=forms.widgets.CheckboxInput(attrs={'class': 'form-control'}),
                                      )
    address = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text",

    }))
    is_active = forms.CharField(required = False)
    serialNumber = forms.CharField(required = False)

    def __init__(self, *args, **kwargs):
        super(DriverSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.other_name = self.cleaned_data.get('other_name')
        user.save()
        driver = Driver.objects.create(user=user)
        result = Driver.objects.get(user_id=driver.user_id)
        driver.dob = self.cleaned_data.get('dob')
        driver.state = self.cleaned_data.get('state')
        driver.lga = self.cleaned_data.get('lga')
        driver.gender = self.cleaned_data.get('gender')
        driver.edQlf = self.cleaned_data.get('edQlf')
        driver.carType = self.cleaned_data.get('carType')
        driver.maritalStatus = self.cleaned_data.get('maritalStatus')
        driver.nok = self.cleaned_data.get('nok')
        driver.serialNumber = str(result.user_id)
        driver.plateNumber = self.cleaned_data.get('plateNumber')
        driver.phoneNumber = self.cleaned_data.get('phoneNumber')
        driver.address = self.cleaned_data.get('address')
        driver.is_car_owner = self.cleaned_data.get('is_car_owner')
        driver.save()
        return user


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    other_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
    }))

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'other_name']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text",
    }))

    class Meta:
        model = Profile
        abstract = False
        fields = ['bio', 'image', 'active']


class PassengerUpdateForm(forms.ModelForm):
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    dob = forms.DateField(widget=NumberInput(attrs={
        'type': "date"

    }))

    def __init__(self, *args, **kwargs):
        super(PassengerUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Passenger
        fields = ['matricNo', 'dob', 'state', 'lga', 'gender', 'phoneNumber', 'address']


class DriverUpdateForm(forms.ModelForm):
    dob = forms.DateField(widget=NumberInput(attrs={
        'type': "date"

    }))
    is_car_owner = forms.BooleanField(label_suffix = " : ",
          disabled = False,
          required = False,
          widget=forms.widgets.CheckboxInput(attrs={'class': 'form-control'}),
                                      )
    is_active = forms.BooleanField(required = False)
    serialNumber = forms.CharField(required = False)

    def __init__(self, *args, **kwargs):
        super(DriverUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Driver
        fields = ['is_active','is_car_owner','plateNumber', 'serialNumber','nok','maritalStatus','carType','edQlf', 'dob', 'state', 'lga', 'gender', 'phoneNumber', 'address']