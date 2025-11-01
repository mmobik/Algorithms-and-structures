class Deque:
    """Класс двойной очереди. Позволяет добавлять и удалять с конца и начала элементы за O(1)"""
    def __init__(self, max_size=0):
        """
        :param max_size: Фиксированный размер очереди.
        """
        self.__max_size = max_size
        self.capacity = [None] * self.max_size
        self.__current_size = 0

        # Указатели на голову и хвост очереди.
        self.head = 0
        self.tail = 0

    @property
    def max_size(self):
        return self.__max_size

    @property
    def current_size(self):
        return self.__current_size

    @current_size.setter
    def current_size(self, value):
        if value is not None:
            self.__current_size = value
        else:
            raise ValueError("Значение не должно быть пустым!")

    def push_back(self, value):
        """Метод добавляет элемент в начало очереди."""
        if self.current_size == self.max_size:
            raise IndexError("Очередь переполнена!")

        self.capacity[self.tail] = value
        self.current_size += 1
        self.tail = (self.tail + 1) % self.max_size

    def push_front(self, value):
        """Метод добавляет элемент в конец очереди."""
        if self.current_size == self.max_size:
            raise IndexError("Очередь переполнена!")

        self.head = (self.head - 1) % self.max_size
        self.capacity[self.head] = value
        self.current_size += 1

    def pop_front(self):
        """Метод извлекает элемент из конца очереди."""
        if self.current_size == 0:
            raise IndexError("Очередь пуста!")

        value = self.capacity[self.head]
        self.capacity[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return value

    def pop_back(self):
        """Метод извлекает элемент из начала очереди."""
        if self.current_size == 0:
            raise IndexError("Очередь пуста!")

        self.tail = (self.tail - 1) % self.max_size
        value = self.capacity[self.tail]
        self.capacity[self.tail] = None
        self.current_size -= 1
        return value
