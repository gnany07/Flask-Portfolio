import smtplib
import sys
import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

SENDER_EMAIL_ID = '*@gmail.com'
SENDER_PASSWORD = '*'


def send_gmail(receiver_name, receiver_email_id, reason):
    try:
        # creates SMTP session
        s = smtplib.SMTP_SSL('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(SENDER_EMAIL_ID, SENDER_PASSWORD)

        # message to be sent
        message = "Thanks" + receiver_name + "! for connecting." + \
            "We can schedule a call and meetup for " + reason

        # sending the mail
        s.sendmail("sender_email_id", receiver_email_id, message)

        # terminating the session
        s.quit()
    except:
        print(sys.exc_info()[0])
        raise


def send_message(receiver_name, receiver_mobile_no, reason):
    try:
        # message to be sent
        body = "Thanks" + receiver_name + "! for connecting." + \
            "We can schedule a call and meetup for " + reason
        print(body)
        message = client.messages \
            .create(
                body=body,
                from_='+14303051409',
                to=receiver_mobile_no
            )
        print(message.sid)
    except:
        print(sys.exc_info()[0])
        raise
