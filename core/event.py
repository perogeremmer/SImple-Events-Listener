import importlib
from abc import ABC
from core.listener import EventListener
from pathlib import Path
import os

class Event(ABC):
    module = ""
    
    # Will continue development on this method
    @classmethod
    def get_files(cls, path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file
    
    # Will continue development on this method
    @classmethod
    def get_listener_name(cls):
        cls_name = cls.__qualname__
        
        listener_name = ""
        
        index = 0
        for item in cls_name:
            _listener_name = ""
            
            if index > 0 and item.isupper():
                _listener_name += "_"
                _listener_name += item.lower()
            elif item.isupper():
                _listener_name += item.lower()
            else:
                _listener_name += item
            
            listener_name += _listener_name
            index += 1
                
        splitted_name = listener_name.split("_")
        length = len(splitted_name)
        splitted_name[length - 1] = "listener"
        
        listener_name = "_".join(splitted_name)
        
        return listener_name

    
    @classmethod
    def before(cls, **kwargs):
        pass

    @classmethod
    def dispatch(cls, payload: dict, **kwargs):
        cls.before(**kwargs)
        cls.handle(payload)
        cls.after(**kwargs)
        
    @classmethod
    def after(cls, **kwargs):
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