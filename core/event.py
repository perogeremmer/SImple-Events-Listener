import importlib
from abc import ABC, abstractmethod
from core.listener import EventListener

class Event(ABC):
    module = ""

    @staticmethod
    @abstractmethod
    def dispatch(self, payload: dict):
        pass
    
    @classmethod
    def handle(cls, payload=None):
        event_listener = EventListener(payload=payload)
        module_import = importlib.import_module(cls.module)
        
        class_name = cls.get_class_name(cls.module)
        
        obj_class = getattr(module_import, cls.get_attribute_class(class_name))
        
        obj = obj_class()
        obj.handle(event_listener.get_payload()) 
        
    @classmethod
    def get_class_name(cls, module):
        split_module =  module.split(".")
        length = len(split_module)
        
        return split_module[length - 1]
        
    @classmethod
    def get_attribute_class(cls, module):
        string_split = module.split("_")
        
        result = ""
        for item in string_split:
            result += item.capitalize()

        return result