from typing import List, Any


def format_numbers(numbers: List[Any], delimiter=" ") -> str:
    """Преобразует массив чисел в строку с указанным разделителем"""
    if not numbers:
        return ""

    result = ""
    for i in range(len(numbers)):
        if i > 0:
            result += delimiter
        result += str(numbers[i])
    return result
