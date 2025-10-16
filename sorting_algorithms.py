"""
Custom sorting algorithms for educational purposes.
Includes Bubble Sort.
"""

def bubble_sort(arr):
    """
    Bubble Sort: Sorts in ascending order.
    Time complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage (for testing):
# bubble_sort([64, 34, 25, 12, 22, 11, 90])
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
