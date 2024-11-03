import time
import random

# Quick Sort Algorithm
def quick_sort(A):
    # Base case: if array has 1 or no elements, it's already sorted
    if len(A) <= 1:
        return A
    
    # Choose pivot as the middle element
    pivot = A[len(A) // 2]
    
    # Partitioning step: elements less than pivot, equal to pivot, and greater than pivot
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    
    # Recursively sort left and right partitions and combine them with the middle
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
A = [7, 6, 8, 10, 3, 2, 4]
print("Sorted array using Quick Sort:", quick_sort(A))

# Generate test datasets
n = 10000  # Set the size of the dataset

sorted_data = list(range(n))
reverse_sorted_data = list(range(n, 0, -1))
random_data = [random.randint(1, n) for _ in range(n)]

# Measure execution time for Quick Sort
start_time = time.time()
quick_sort(sorted_data)
print(f"Quick Sort (Sorted Data): {time.time() - start_time:.6f} seconds")

start_time = time.time()
quick_sort(reverse_sorted_data)
print(f"Quick Sort (Reverse Sorted Data): {time.time() - start_time:.6f} seconds")

start_time = time.time()
quick_sort(random_data)
print(f"Quick Sort (Random Data): {time.time() - start_time:.6f} seconds")
