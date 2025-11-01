from typing import Iterable, Any


def list(iter_object: Iterable[Any]):
    result = []
    if hasattr(iter_object, "__iter__"):
        for element in iter_object:
            result.append(element)
        return result
    else:
        return None
