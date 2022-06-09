from core.listener import EventListener

class SendEmailListener(EventListener):
    def handle(self, payload: dict):
        print(payload)