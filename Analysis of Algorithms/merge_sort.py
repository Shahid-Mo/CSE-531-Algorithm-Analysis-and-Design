def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    This function recursively splits the array into halves, sorts each half, and merges them.

    Parameters:
    arr (list): The list of elements to be sorted.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        merge(arr, left_half, right_half)  # Merging the sorted halves

def merge(arr, left, right):
    """
    Merges two sorted sub-arrays into a single sorted array.
    
    Parameters:
    arr (list): The original list that needs to be merged and sorted.
    left (list): The left sub-array.
    right (list): The right sub-array.
    """
    i = j = k = 0  # i - to mark the index of left sub-array, j - right sub-array, k - merged array

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
if __name__ == "__main__":
    my_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", my_array)
    merge_sort(my_array)
    print("Sorted array:", my_array)
