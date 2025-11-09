"""
Data Structures & Algorithms Library
Профессиональные реализации структур данных и алгоритмов
"""

from .Structures import (
    HashTable,
    Set,
    Tuple,
    Deque,
    LinkedList,
    MaxHeap,
    MinHeap
)

from .Algorithms import (
    Enumerate,
    merge_sort,
    quick_sort,
    quick_sort_inplace,
    format_numbers,
    join, parser_numbers
)

__all__ = [
    'HashTable', 'Set', 'Tuple', 'Deque', 'LinkedList', 'MaxHeap', 'MinHeap',
    'Enumerate', 'merge_sort', 'quick_sort', 'quick_sort_inplace',
    'format_numbers', 'join', 'parser_numbers'
]

__version__ = "1.0.1"
