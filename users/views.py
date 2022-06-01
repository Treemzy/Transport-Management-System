from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User, Passenger, Driver
from .forms import ( PassengerSignUpForm,
                     DriverSignUpForm,
                     ProfileUpdateForm,
                     UserUpdateForm,
                     PassengerUpdateForm,
                     DriverUpdateForm,
                     )
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def success(request):
    return render(request, 'users/success.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Username or Password is Incorrect!')
    return render(request, 'users/login.html')


def LogOut(request):
    logout(request)
    return redirect('home')


class passenger_register(CreateView):
    model = User
    form_class = PassengerSignUpForm
    template_name = 'users/passenger_register.html'


class driver_register(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'users/driver_register.html'

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if request.user.is_passenger:
            ps_form = PassengerUpdateForm(request.POST, instance=request.user.passenger)
            if u_form.is_valid() and p_form.is_valid() and ps_form.is_valid():
                u_form.save()
                ps_form.save()
                p_form.save()
                username = u_form.cleaned_data.get('username')
                messages.success(request, f' {username} Your account has been Updated !')
                return redirect('profile')
        elif request.user.is_driver:
            ds_form = DriverUpdateForm(request.POST, instance=request.user.driver)
            if u_form.is_valid() and p_form.is_valid() and ds_form.is_valid():
                u_form.save()
                ds_form.save()
                p_form.save()
                username = u_form.cleaned_data.get('username')
                messages.success(request, f' {username} Your account has been Updated !')
                return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    if request.user.is_passenger:
        ps_form = PassengerUpdateForm(instance=request.user.passenger)
    elif request.user.is_driver:
        ds_form = DriverUpdateForm(instance=request.user.driver)
    if request.user.is_passenger:
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'ps_form': ps_form,
        }
    elif request.user.is_driver:
        context = {
            'u_form': u_form,
            'p_form': p_form,
            'ds_form': ds_form,
        }
    else:
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
    return render(request, 'users/profile.html', context)
