from django.urls import path
from . import views
from .views import (
    TripListView,
    TripDetailView,
    # PaymentView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('trip/', views.initiate_payment, name='home'),
    path('transaction/', TripListView.as_view(), name='transaction'),
    # path('payment/', PaymentView.as_view(), name='payment'),
    path('transaction/<int:pk>/', TripDetailView.as_view(), name='Transaction-Detail'),
    path('<str:ref>/', views.verify_payment, name="verify-payment"),
]
