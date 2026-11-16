def quicksort(arr):
    """
    Sorts an array using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        New sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sorts an array in-place using the quicksort algorithm.
    
    Args:
        arr: List to be sorted
        low: Starting index
        high: Ending index
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    """
    Partition function for in-place quicksort.
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage and tests
if __name__ == "__main__":
    # Test the quicksort function
    test_array = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original array: {test_array}")
    
    sorted_array = quicksort(test_array)
    print(f"Sorted array: {sorted_array}")
    
    # Test in-place version
    test_array2 = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original array (in-place): {test_array2}")
    quicksort_inplace(test_array2)
    print(f"Sorted array (in-place): {test_array2}")
