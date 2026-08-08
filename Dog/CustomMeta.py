class CustomMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.new_attribute = "This is a new attribute."
        return instance

class MyClass(metaclass=CustomMeta):
    pass

obj = MyClass()
print(obj.new_attribute)