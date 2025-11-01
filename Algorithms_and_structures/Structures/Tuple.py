class TupleIterator:
    def __init__(self, elements):
        """
        :param elements: Элементы кортежа. Используем композицию.
        """
        self.index = 0
        # Делаем элементы кортежа итерируемыми
        self.elements = elements

    def __iter__(self):
        """Итератор по протоколу итератор должен возвращать сам себя"""
        return self

    def __next__(self):
        if self.index < len(self.elements):
            value = self.elements[self.index]
            self.index += 1
            return value
        raise StopIteration

class Tuple:
    """Класс кортежа. Не позволяет изменять данные после инициализации."""
    def __init__(self, *elements):
        """
        :param elements: произвольные элементы кортежа
        """
        self.__length = 0
        self.elements = []
        for element in elements:
            self.elements.append(element)
            self.__length += 1

    @property
    def length(self):
        return self.__length

    def __getitem__(self, index):
        """Магический метод для получения элемента кортежа по индексу"""
        return self.elements[index]

    def __len__(self):
        """Магический метод для получения длины кортежа через len"""
        return self.length

    def __iter__(self):
        """Итератор по протоколу должен возвращать сам себя.
        Ссылается на класс итератора"""
        return TupleIterator(self.elements)

    def __repr__(self):
        """Метод для абстракции и удобного представления кортежа"""
        elements_str = ""
        current_index = 0
        last_index = len(self) - 1
        for el in self.elements:
            if current_index == last_index:
                elements_str += str(el)
            else:
                elements_str += f"{el}, "
            current_index += 1
        return f"({elements_str})"

    def __eq__(self, other):
        """Метод для сравнения кортежей"""
        if not isinstance(other, Tuple):
            return False
        else:
            if len(self) == len(other):
                count = 0
                for el in self:
                    if el != other[count]:
                        return False
                    else:
                        count += 1
                return True
            return False
