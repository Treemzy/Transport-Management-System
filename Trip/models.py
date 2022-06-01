import secrets
from .paystack import PayStack
from django.db import models
from django.utils import timezone
from users.models import Driver
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class Start(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name


class End(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    createDate = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    start = models.ForeignKey(Start, null=True, on_delete=models.SET_NULL)
    end = models.ForeignKey(End, null=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createDate = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-createDate',)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Trip.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount *100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False