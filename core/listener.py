class EventListener(object):
    def __init__(self, payload=None):
        self.__payload = payload
        
    def get_payload(self):
        return self.__payload