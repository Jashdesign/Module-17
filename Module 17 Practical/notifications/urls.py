from django.urls import path
from .views import send_otp_api, verify_otp_api

urlpatterns = [
    path('send-otp/', send_otp_api),
    path('verify-otp/', verify_otp_api),
]