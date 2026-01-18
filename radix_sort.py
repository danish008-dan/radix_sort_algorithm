"""
File Name   : radix_sort.py
Purpose     : Implementation of Radix Sort algorithm using Counting Sort
Description : Radix Sort is a non-comparison based sorting algorithm that
              sorts numbers digit by digit (from least significant digit
              to most significant digit). It is efficient for sorting
              large datasets with integers.
"""

def counting_sort_for_radix(arr, exp):
    """
    This function performs Counting Sort based on the digit
    represented by exp (1, 10, 100, etc.)
    """

    n = len(arr)                     # Store length of array
    output = [0] * n                 # Output array to store sorted result
    count = [0] * 10                 # Count array for digits 0-9

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10 # Extract digit at current place value
        count[index] += 1            # Increment count for that digit

    # Modify count array to store cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]     # Update count to position elements correctly

    # Build output array (right to left to maintain stability)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10 # Extract digit again
        output[count[index] - 1] = arr[i]  # Place element at correct position
        count[index] -= 1            # Decrease count
        i -= 1

    # Copy sorted values back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Main Radix Sort function that sorts the array
    by processing digits from least to most significant
    """

    max_num = max(arr)               # Find maximum number in array
    exp = 1                          # Initialize exponent (1, 10, 100...)

    # Apply counting sort for each digit
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)  # Sort based on current digit
        exp *= 10                   # Move to next digit place


# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    print("Original Array:")
    print(arr)

    radix_sort(arr)                  # Call Radix Sort

    print("Sorted Array:")
    print(arr)
