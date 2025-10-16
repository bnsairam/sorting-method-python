#!/usr/bin/env python3
"""
Simple Sorting Method in Python.
Sorts user-input lists in ascending or descending order.
"""

import sys
from sorting_algorithms import bubble_sort  # Optional custom sort

def get_user_input():
    """Get comma-separated input from user."""
    while True:
        user_input = input("Enter a list of items separated by commas (e.g., 5,2,8,1 or apple,banana,cherry): ").strip()
        if user_input:
            try:
                # Try parsing as numbers first
                items = [float(x.strip()) for x in user_input.split(',')]
                print("Parsing as numbers.")
            except ValueError:
                # Fallback to strings
                items = [x.strip() for x in user_input.split(',')]
                print("Parsing as strings.")
            return items
        print("Invalid input. Please try again.")

def sort_list(items, order='asc', method='built-in'):
    """Sort the list based on order and method."""
    if method == 'built-in':
        if order == 'asc':
            return sorted(items)
        else:
            return sorted(items, reverse=True)
    elif method == 'bubble':
        if order == 'desc':
            # Bubble sort ascending then reverse for descending
            bubble_sort(items)
            return sorted(items, reverse=True)
        else:
            bubble_sort(items)
            return items

def main():
    print("Welcome to the Python Sorting Method!")
    items = get_user_input()
    
    print("\nOriginal list:", items)
    
    order = input("\nSort order (asc/desc): ").strip().lower()
    if order not in ['asc', 'desc']:
        print("Defaulting to ascending.")
        order = 'asc'
    
    method = input("Sort method (built-in/bubble): ").strip().lower()
    if method not in ['built-in', 'bubble']:
        print("Defaulting to built-in.")
        method = 'built-in'
    
    sorted_items = sort_list(items, order, method)
    print(f"\nSorted list ({order}ending using {method}):", sorted_items)

if __name__ == "__main__":
    main()
