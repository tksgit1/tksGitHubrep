class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.limit:
            raise StopIteration

        x = self.n
        self.n += 2
        return x


# Create an iterator for even numbers up to 10
even = EvenNumbers(10)

for num in even:
    print(num)
