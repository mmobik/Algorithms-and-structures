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
    MinHeap,
    OptimizedHashTable
)

from .Algorithms import (
    Enumerate,
    merge_sort,
    quick_sort,
    quick_sort_inplace,
    format_numbers,
    join, parser_numbers,
    validate_inputs
)

__all__ = [
    'HashTable', 'Set', 'Tuple', 'Deque', 'LinkedList', 'MaxHeap', 'MinHeap',
    'Enumerate', 'merge_sort', 'quick_sort', 'quick_sort_inplace',
    'format_numbers', 'join', 'parser_numbers', 'validate_inputs', 'OptimizedHashTable'
]

__version__ = "1.0.3"
