from typing import List


def parser_numbers(input_string: str, delimiter=" ") -> List[int]:
    """Функция преобразует строку с указанным разделителем в массив чисел"""
    if delimiter == "":
        try:
            return [int(input_string)]
        except ValueError:
            raise ValueError("Преобразовать данную строку с таким разделителем невозможно")

    elif input_string == "":
        return []

    current_string = ""
    numbers = []

    for char in input_string:
        if char == delimiter:
            if current_string != "":
                try:
                    numbers.append(int(current_string))
                except ValueError:
                    raise ValueError("Неверный формат входных данных")
                current_string = ""
        else:
            current_string += char

    if current_string:
        numbers.append(int(current_string))
    return numbers
