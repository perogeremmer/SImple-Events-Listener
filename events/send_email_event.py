from core.event import Event

class SendEmailEvent(Event):    
    module = "listeners.send_email_listener"
    
    @classmethod
    def before(cls, **kwargs):
        print("Before method")
        
    @classmethod
    def after(cls, **kwargs):
        print("after method")