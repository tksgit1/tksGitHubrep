class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)
