# Основные импорты. Данные алгоритмы и методы написаны вручную.
from ..Algorithms import Enumerate
from .Tuple import Tuple


class HashTableIterator:
    """Класс-итератор для хеш-таблицы"""
    def __init__(self, buckets):
        """
        :param buckets: Бакеты переданные из хеш-таблицы. Используется композиция.
        """
        self.buckets = buckets
        self.bucket_index = 0
        self.element_index = 0

    def __iter__(self):
        """По протоколу должен возвращать сам себя"""
        return self

    def __next__(self):
        """Каждый итератор должен иметь метод next"""
        while self.bucket_index < len(self.buckets):
            bucket = self.buckets[self.bucket_index]
            if self.element_index < len(bucket):
                element = bucket[self.element_index]
                self.element_index += 1
                # В данном случае мы возвращаем только ключ.
                return element[0]
            else:
                self.bucket_index += 1
                self.element_index = 0
        raise StopIteration


class HashTable:
    """Класс хеш-таблицы. Позволяет добавлять и удалять пары ключ - значение примерно за O(1)"""
    def __init__(self, capacity=10):
        """
        :param capacity: Изначальный размер хеш-таблицы.
        """
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        # Текущий размер хеш-таблицы.
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value is None:
            raise ValueError("Значение не должно быть None.")
        self.__size = value

    def __hash(self, key, base=31):
        """Метод считает полиномиальный хеш для строк и простой хеш для чисел."""
        _hash_value = 0
        if isinstance(key, int):
            return key % self.capacity
        # Схема Горнера
        for char in key:
            _hash_value = _hash_value * base + ord(char)
        return _hash_value % self.capacity

    def put(self, key, value):
        """Метод добавляет пару ключ-значение в бакет."""
        # Считает коэффициент переполнения
        ratio = self.size / self.capacity
        # Если коэффициент больше 0.7, то увеличиваем размер хеш-таблицы в 2 раза.
        if ratio > 0.7:
            self.capacity *= 2
            new_buckets = [[] for _ in range(self.capacity)]
            # Передаем в новые бакеты старые значения.
            for bucket in self.buckets:
                for existing_key, existing_value in bucket:
                    index = self.__hash(existing_key)
                    new_buckets[index].append(Tuple(existing_key, existing_value))
            self.buckets = new_buckets

        # Ищем нужный бакет.
        index = self.__hash(key)
        bucket = self.buckets[index]

        # Добавляем в нужный бакет наши значения.
        for i, tuple_element in Enumerate(bucket):
            existing_key = tuple_element[0]
            if existing_key == key:
                bucket[i] = Tuple(key, value)
                return
        bucket.append(Tuple(key, value))
        self.size += 1

    def get(self, key):
        """Метод получает значение при передаче правильного ключа"""
        # Ищем нужный бакет.
        index = self.__hash(key)
        bucket = self.buckets[index]

        # Ищем нужный ключ внутри бакета
        for current_key, current_value in bucket:
            if key == current_key:
                return current_value
        return None

    def delete(self, key):
        """Метод удаляет пару ключ-значение при передаче правильного ключа"""
        # Ищем нужный бакет.
        index = self.__hash(key)
        bucket = self.buckets[index]

        # Ищем нужный ключ внутри бакета
        for i, tuple_element in Enumerate(bucket):
            current_key = tuple_element[0]
            if key == current_key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __iter__(self):
        """Магический метод возвращает итератор. Нужен для итерации по объекту"""
        return HashTableIterator(self.buckets)

    def __len__(self):
        """Магический метод возвращает текущий размер хеш-таблицы"""
        return self.size

    def __repr__(self):
        """Магический метод служит для более красивого вывода хеш-таблицы. Для абстракции."""
        if len(self) == 0:
            return "{}"

        result = "{"
        count = 0
        index_count = len(self) - 1
        for bucket in self.buckets:
            for tuple_element in bucket:
                existing_key = tuple_element[0]
                existing_value = tuple_element[1]
                if count == index_count:
                    result += f"{existing_key}: {existing_value}" + "}"
                else:
                    result += f"{existing_key}: {existing_value}, "
                count += 1
        return result
