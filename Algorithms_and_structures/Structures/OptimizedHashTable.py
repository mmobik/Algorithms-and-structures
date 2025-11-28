class OptimizedHashTable:
    """Оптимизированная хеш-таблица для операций с базой данных."""
    def __init__(self, capacity=100000):
        """
        Инициализация хеш-таблицы с заданной емкостью.
        
        :param capacity: Начальная емкость для минимизации операций рехеширования
        """
        self.capacity = capacity
        # Использование простых списковых структур для оптимальной производительности
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.size = 0

    def __hash(self, key):
        """Первичная хеш-функция, оптимизированная для алфавитно-цифровых ключей."""
        if isinstance(key, int):
            return key % self.capacity
        
        # Оптимизированное вычисление хеша для ASCII символов
        h = 0
        for char in key:
            h = (h * 31 + ord(char)) % self.capacity
        return h

    def __secondary_hash(self, key):
        """Вторичная хеш-функция для разрешения коллизий методом двойного хеширования."""
        if isinstance(key, int):
            return 1 + (key % (self.capacity - 1))
        
        h = 5381
        for char in key:
            h = (h * 33 + ord(char)) % (self.capacity - 1)
        return 1 + h

    def put(self, key, value):
        """Вставка или обновление пары ключ-значение с использованием двойного хеширования."""
        if self.size >= self.capacity * 0.7:
            self._resize()
            
        hash1 = self.__hash(key)
        hash2 = self.__secondary_hash(key)
        
        for i in range(self.capacity):
            idx = (hash1 + i * hash2) % self.capacity
            
            if self.keys[idx] is None:
                # Найдена свободная ячейка - вставка новой записи
                self.keys[idx] = key
                self.values[idx] = value
                self.size += 1
                return
            elif self.keys[idx] == key:
                # Ключ существует - обновление значения
                self.values[idx] = value
                return

    def get(self, key):
        """Получение значения, связанного с указанным ключом."""
        hash1 = self.__hash(key)
        hash2 = self.__secondary_hash(key)
        
        for i in range(self.capacity):
            idx = (hash1 + i * hash2) % self.capacity
            
            if self.keys[idx] is None:
                return None
            elif self.keys[idx] == key:
                return self.values[idx]
        return None

    def delete(self, key):
        """Удаление пары ключ-значение с использованием маркера удаления."""
        hash1 = self.__hash(key)
        hash2 = self.__secondary_hash(key)
        
        for i in range(self.capacity):
            idx = (hash1 + i * hash2) % self.capacity
            
            if self.keys[idx] is None:
                return False
            elif self.keys[idx] == key:
                # Пометка записи как удаленной с использованием специального значения
                self.keys[idx] = "__DELETED__"
                self.values[idx] = None
                self.size -= 1
                return True
        return False

    def _resize(self):
        """Изменение размера хеш-таблицы и рехеширование всех существующих записей."""
        old_keys = self.keys
        old_values = self.values
        
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        
        # Перенос только действительных записей, исключая маркеры удаления
        for i in range(len(old_keys)):
            if old_keys[i] is not None and old_keys[i] != "__DELETED__":
                self.put(old_keys[i], old_values[i])

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None
