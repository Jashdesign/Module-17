from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import send_otp, verify_otp

@api_view(['POST'])
def send_otp_api(request):
    phone = request.data.get("phone")

    if not phone:
        return Response(
            {"error": "Phone number is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    send_otp(phone)
    return Response({"message": "OTP sent successfully"})


@api_view(['POST'])
def verify_otp_api(request):
    phone = request.data.get("phone")
    otp = request.data.get("otp")

    if not phone or not otp:
        return Response(
            {"error": "Phone and OTP required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if verify_otp(phone, otp):
        return Response({"message": "OTP verified"})
    else:
        return Response(
            {"error": "Invalid OTP"},
            status=status.HTTP_400_BAD_REQUEST
        )