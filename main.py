from events.send_email_event import SendEmailEvent


print("Registering....")

payload = {
    "name": "Hudya"
}

SendEmailEvent.dispatch(payload)