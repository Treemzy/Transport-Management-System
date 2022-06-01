from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from . import forms
from django.conf import settings
from .models import Trip
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'Trip/home.html')


def home(request):
    return render(request, 'Trip/index.html')


def trip(request):
    return render(request, 'Trip/Trans.html')


class TripListView(LoginRequiredMixin,ListView):
    model = Trip
    context_object_name = 'trip'
    ordering = ['-createDate']
    template_name = 'Trip/Trans.html'
    paginate_by = 10

    def get_queryset(self):
        return Trip.objects.filter(creator=self.request.user).order_by('-createDate')


# class PaymentView(ListView):
#     model = Trip
#     context_object_name = 'trip'
#     ordering = ['-createDate']
#     template_name = 'Trip/payments.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return Trip.objects.filter(creator=self.request.user).order_by('-createDate')


class TripDetailView(LoginRequiredMixin,DetailView):
    model = Trip
    context_object_name = 'trip'
    template_name = 'Trip/TransDetail.html'


@login_required
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'Trip/make_payment.html', {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'Trip/index.html', {'payment_form': payment_form})


@login_required
def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Trip, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Your Payments Was Successfully")
    else:
        messages.error(request, "Verification Failed")
    return redirect('home')







