class AnnotatedClass:
    def __init__(self, a: int, b: str, c: float):
        pass


def count_annotated_init_args(cls):
    init_method = cls.__init__
    annotations = init_method.__annotations__

    # Exclude 'return' annotation and count the remaining ones
    return len(annotations)


num_args = count_annotated_init_args(AnnotatedClass)
print(f"Number of explicit arguments in __init__: {num_args}")