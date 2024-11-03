import time
import random


# Merge Sort Algorithm
def merge_sort(A):
    # Base case: if array has 1 or no elements, it's already sorted
    if len(A) <= 1:
        return A
    
    # Divide the array into two halves
    middle = len(A) // 2
    left_half = merge_sort(A[:middle])
    right_half = merge_sort(A[middle:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge two sorted arrays by comparing elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append any remaining elements from both halves
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
A = [7, 6, 8, 10, 3, 2, 4]
print("Sorted array using Merge Sort:", merge_sort(A))


# Generate test datasets
n = 10000  # Set the size of the dataset

sorted_data = list(range(n))
reverse_sorted_data = list(range(n, 0, -1))
random_data = [random.randint(1, n) for _ in range(n)]

# Measure execution time for Merge Sort
start_time = time.time()
merge_sort(sorted_data)
print(f"Merge Sort (Sorted Data): {time.time() - start_time:.6f} seconds")

start_time = time.time()
merge_sort(reverse_sorted_data)
print(f"Merge Sort (Reverse Sorted Data): {time.time() - start_time:.6f} seconds")

start_time = time.time()
merge_sort(random_data)
print(f"Merge Sort (Random Data): {time.time() - start_time:.6f} seconds")
