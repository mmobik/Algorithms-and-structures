# Используем хеш-таблицу для создания множества
from .HashTable import HashTable

class Set:
    """Класс множества. Аналог встроенного множества, но написанный вручную."""
    def __init__(self, start_elements=None, capacity=10):
        """
        :param start_elements: Элементы множества сразу после инициализации
        :param capacity: размер нашего множества
        """
        # Используем композицию для доступа ко всем фичам хеш-таблицы
        self.hashtable = HashTable(capacity)
        if start_elements is not None:
            self.add(start_elements)

    def add(self, element):
        """Метод добавления элемента во множество."""
        # Если объект итерируемый, то добавляем все его элементы по очереди.
        if hasattr(element, "__iter__") and not isinstance(element, str):
            for el in element:
                self.hashtable.put(el, el)
        else:
            self.hashtable.put(element, element)

    def contains(self, element):
        """Метод для проверки присутствия элемента во множестве."""
        return self.hashtable.get(element) is not None

    def remove(self, element):
        """Метод удаляет элемент из множества."""
        self.hashtable.delete(element)

    @property
    def size(self):
        return self.hashtable.size

    @size.setter
    def size(self, value):
        if value is None:
            raise ValueError("Значение не должно быть None.")
        self.size = value

    def is_empty(self):
        """Метод проверяет пусто ли множество."""
        return self.size == 0

    def symmetric_difference(self, other):
        """Метод симметрической разности двух множеств."""

        # Установим так, чтобы было меньше операций расширения множества.
        result = Set(capacity=max(1, (self.size + other.size) // 2))

        # Проверяем первое множество.
        for bucket in self.hashtable.buckets:
            if bucket:
                for key, _ in bucket:
                    # Проверяем нет ли во втором множестве элементов первого.
                    if not other.contains(key):
                        result.add(key)

        # Проверяем второе множество.
        for bucket in other.hashtable.buckets:
            if bucket:
                for key, _ in bucket:
                    # Проверяем нет ли в первом множестве элементов второго.
                    if not self.contains(key):
                        result.add(key)
        return result

    def intersection(self, other):
        """Метод пересечения двух множеств."""
        result = Set(capacity=max(1, (self.size + other.size) // 2))

        for bucket in self.hashtable.buckets:
            if bucket:
                for k, v in bucket:
                    if other.contains(k):
                        result.add(k)
        return result

    def difference(self, other):
        """Метод разности множеств.
        Возвращает элементы первого множества, которые не присутствуют во втором."""
        result = Set(capacity=max(1, (self.size + other.size) // 2))

        for bucket in self.hashtable.buckets:
            if bucket:
                for k, v in bucket:
                    if not other.contains(k):
                        result.add(k)
        return result

    def union(self, other):
        """Метод объединения двух множеств. Возвращает новое множество уникальных элементов."""
        result = Set(capacity=max(1, (self.size + other.size) // 2))
        for bucket in self.hashtable.buckets:
            for k, v in bucket:
                result.add(k)
        for bucket in other.hashtable.buckets:
            for k, v in bucket:
                if not self.contains(k):
                    result.add(k)
        return result

    def __iter__(self):
        """Итератор множества. Используется итератор хеш-таблицы."""
        return iter(self.hashtable)

    def __len__(self):
        """Магический метод len. Для удобного подсчета размера."""
        return self.hashtable.size

    def __repr__(self):
        """Магический метод для абстракции множества."""
        if len(self) == 0:
            return "{}"

        result = "{"
        count = 0
        index_count = len(self) - 1
        for bucket in self.hashtable.buckets:
            for tuple_element in bucket:
                existing_key = tuple_element[0]
                if count == index_count:
                    result += f"{existing_key}" + "}"
                else:
                    result += f"{existing_key}, "
                count += 1
        return result
