class DynamicMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        if "new_method" in kwargs:
            setattr(instance, kwargs["new_method"], lambda: print("Dynamic method added!"))
        return instance

class DynamicClass(metaclass=DynamicMeta):
    def __init__(self, *args, **kwargs):
        pass

obj = DynamicClass(new_method="dynamic_method")
obj.dynamic_method()