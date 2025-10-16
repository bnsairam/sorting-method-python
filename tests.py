"""
Simple tests for the sorting project.
Run with: python -m pytest tests.py (requires pytest installed)
"""

from main import sort_list
from sorting_algorithms import bubble_sort

def test_builtin_asc():
    assert sort_list([3, 1, 2], 'asc', 'built-in') == [1, 2, 3]

def test_builtin_desc():
    assert sort_list([3, 1, 2], 'desc', 'built-in') == [3, 2, 1]

def test_bubble_asc():
    arr = [3, 1, 2]
    bubble_sort(arr)
    assert arr == [1, 2, 3]

if __name__ == "__main__":
    test_builtin_asc()
    test_builtin_desc()
    test_bubble_asc()
    print("All tests passed!")
