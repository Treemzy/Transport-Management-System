from django import forms
from crispy_forms.helper import FormHelper
from django.db.models import Count

from .models import Trip
from users.models import Driver
import django_filters


class PaymentForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.Select(attrs={
        })
    )

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Trip
        fields = ['amount', 'email', 'start', 'end', 'vehicle', 'creator', 'createDate']
