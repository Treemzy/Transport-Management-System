from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import (
#
#
# )

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('success/', views.success, name='congrats'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('passenger_register/', views.passenger_register.as_view(), name='passenger_register'),
    path('driver_register/', views.driver_register.as_view(), name='driver_register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    # path('Role/', RoleListView.as_view(), name='TMS-Role'),
    # path('AllUsers/', UsersListView.as_view(), name='TMS-AllUsers'),
]
