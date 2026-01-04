import random
import os
from twilio.rest import Client

# Temporary in-memory storage (for learning purpose)
OTP_STORE = {}

def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    OTP_STORE[phone_number] = otp

    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=phone_number
    )

    return True


def verify_otp(phone_number, otp):
    return OTP_STORE.get(phone_number) == int(otp)