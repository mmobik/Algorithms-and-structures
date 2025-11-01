from typing import Iterable, Iterator, Any


class Enumerate:
    """Аналог встроенной enumerate() в виде класса-итератора."""

    def __init__(self, iter_object: Iterable[Any]):
        self.index = 0
        self.iter_object = iter(iter_object)

    def __iter__(self) -> Iterator[list]:
        return self

    def __next__(self) -> list:
        try:
            value = next(self.iter_object)
            result = [self.index, value]
            self.index += 1
            return result
        except StopIteration:
            raise StopIteration

