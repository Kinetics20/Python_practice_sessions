# TODO iterable protocol -> __iter__ -> iterator object
# TODO iterator protocol -> __iter__ & __next__ -> item | StopIteration


numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for idx, number in enumerate(iterator):
#     print(idx, number)

class Range:
    def __init__(self, start: int, stop: int | None = None, step: int = 1, /) -> None:
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.stop = stop
        self.step = step

        self.item = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.item >= self.stop:
            raise StopIteration('Sth is wrong')

        result = self.item

        self.item += self.step

        return result

r1 = Range(0, 5, 2)
it = iter(r1)
print(r1 is it)
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))

# for element in Range(5):
#     print(element)


