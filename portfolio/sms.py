import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_sms(message): # add phone number as argument 
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body = message,
                        from_ = '+15674832537',
                        to = '+2348131542720'
                    )

    return message.sid