class Odd:
    def __init__(self, iterable):
        self.iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.iterable):
            raise StopIteration()



class Iterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

# for element in Iterable([1, 2, 3, 4, 5, 6]):
for element in Iterable({'a': 1, 'b': 2, 'c': 3, 'd': 4}):
    print(element)