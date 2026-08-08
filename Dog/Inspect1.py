import inspect


class AnotherClass:
    def __init__(self, x, y, z):
        pass


def count_init_args_from_source(cls):
    init_method = cls.__init__

    # Get the signature of the __init__ method
    sig = inspect.signature(init_method)

    # Get the parameters from the signature, excluding 'self'
    params = [p for p in sig.parameters.values() if p.name != 'self']

    return len(params)


num_args = count_init_args_from_source(AnotherClass)
print(f"Number of explicit arguments in __init__: {num_args}")