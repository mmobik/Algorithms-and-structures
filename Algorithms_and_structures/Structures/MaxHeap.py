class MaxHeap:
    """
    Реализация max-heap (кучи с максимальным элементом в корне).

    Max-heap - это двоичное дерево, где:
    - Каждый родитель >= своих детей
    - Максимум всегда находится в корне (индекс 0)
    - Эффективные операции: add O(log n), delete O(log n), find_max O(1)

    Использует массив для хранения элементов с формулами:
    - Родитель: (i-1)//2
    - Левый ребенок: 2*i + 1
    - Правый ребенок: 2*i + 2
    """

    def __init__(self):
        """Инициализирует пустую кучу."""
        self.heap_elements = []

    def add(self, value: int):
        """Добавляет элемент в кучу."""
        self.heap_elements.append(value)
        current_index = self.length - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            parent = self.heap_elements[parent_index]
            current = self.heap_elements[current_index]
            if current > parent:
                self.heap_elements[parent_index] = current
                self.heap_elements[current_index] = parent
                current_index = parent_index
            else:
                break

    def delete(self) -> int:
        """Удаляет и возвращает максимальный элемент."""
        max_element = self.find_max()
        self.heap_elements[0] = self.heap_elements[self.length - 1]
        del self.heap_elements[self.length - 1]
        current_index = 0

        while True:
            parent = self.heap_elements[current_index]
            try:
                left_child = self.heap_elements[current_index * 2 + 1]
            except IndexError:
                left_child = None
            try:
                right_child = self.heap_elements[current_index * 2 + 2]
            except IndexError:
                right_child = None

            if left_child is None and right_child is None:
                break

            max_child = max(left_child, right_child)

            if max_child == left_child:
                if parent <= left_child and left_child:
                    self.heap_elements[current_index] = left_child
                    self.heap_elements[current_index * 2 + 1] = parent
                    current_index = current_index * 2 + 1
                else:
                    break
            else:
                if parent <= right_child and right_child:
                    self.heap_elements[current_index] = right_child
                    self.heap_elements[current_index * 2 + 2] = parent
                    current_index = current_index * 2 + 2
                else:
                    break

        return max_element

    def find_max(self) -> int:
        """Возвращает максимальный элемент без удаления."""
        if self.length == 0:
            raise ValueError("Куча должна содержать хотя бы 1 элемент.")
        return self.heap_elements[0]

    @property
    def length(self) -> int:
        """Возвращает количество элементов в куче."""
        return len(self.heap_elements)