import random

def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        less = [i for i in arr if i < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + equal + quick_sort(greater)
