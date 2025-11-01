from typing import Iterable, Any
from .Enumerate import Enumerate


def join(items: Iterable[Any], delimiter=",") -> str:
    """Аналог встроенной функции join"""
    if not items:
        return ""

    str_items = [str(item) for item in items]

    length = 0
    for el in str_items:
        length += len(el)

    length += len(delimiter) * (len(str_items) - 1)

    buffer = [""] * length
    current_position = 0

    for i, item_str in Enumerate(str_items):
        if i > 0:
            for char in delimiter:
                buffer[current_position] = char
                current_position += 1

        for char in item_str:
            buffer[current_position] = char
            current_position += 1

    result = ""
    for char in buffer:
        result += char
    return result
