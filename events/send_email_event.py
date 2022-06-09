from core.event import Event

class SendEmailEvent(Event):    
    module = "listeners.send_email_listener"
    
    @classmethod
    def dispatch(cls, payload: dict):
        cls.handle(payload)