import random

# Randomized Quicksort implementation
def randomized_quicksort(arr):
    """
    Sorts the array using Randomized Quicksort.
    Handles edge cases such as repeated elements, empty arrays, and already sorted arrays.
    """
    if len(arr) <= 1:
        return arr  # Base case: if the array has 0 or 1 element, it is already sorted
    
    # Choose pivot randomly to ensure a balanced partition on average
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Partition the array around the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    # Recursively sort 'less' and 'greater' partitions
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Example usage:
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    sorted_arr = randomized_quicksort(arr)
    print("Sorted array:", sorted_arr)
# Time Complexity Analysis:
# Randomized Quicksort has an average-case time complexity of O(n log n).
#
# Here's why:
# - By choosing the pivot randomly, we increase the probability of balanced partitions,
#   meaning that on average, each recursive call divides the array roughly in half.
#
# - With n elements, the recurrence relation is:
#     T(n) = 2T(n/2) + O(n)
#   where O(n) represents the time needed to partition the array around the pivot.
#
# - Solving this recurrence relation yields T(n) = O(n log n).
#
# - The random choice of pivot ensures that we avoid the worst-case performance (O(n^2)),
#   which occurs when the pivot consistently divides the array unevenly.
#
# - Handling cases like repeated elements, empty arrays, and already sorted arrays
#   improves the robustness of this implementation.

