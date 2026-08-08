import inspect


class ExampleClass:
    def __init__(self, arg1, arg2, arg3):
        pass


def count_init_args(cls):
    init_method = cls.__init__
    if not callable(init_method):
        return 0
    init_signature = inspect.signature(init_method)

    # Exclude 'self' and return the count of parameters
    return len(init_signature.parameters) - 1


num_args = count_init_args(ExampleClass)
print(f"Number of explicit arguments in __init__: {num_args}")