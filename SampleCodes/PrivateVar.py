
class Example:
    def __init__(self):
        self._value = "Internal data"

    def get_value(self):
        return self._value

obj = Example()
print(obj.get_value())

