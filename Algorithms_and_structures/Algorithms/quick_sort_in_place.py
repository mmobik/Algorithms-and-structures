import random

def quick_sort_inplace(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low >= high: return

    # Простой random pivot
    pivot_idx = random.randint(low, high)
    pivot = arr[pivot_idx]

    # Простой partition без лишних swap'ов
    i, j = low, high
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort_inplace(arr, low, j)
    quick_sort_inplace(arr, i, high)
