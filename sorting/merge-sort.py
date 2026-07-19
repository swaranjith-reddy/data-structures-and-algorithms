def merge_sort(arr):
    # The Base Case: If the array is size 1 or 0, it is already sorted.
    if len(arr) <= 1:
        return arr

    # --- PHASE 1: THE SPLIT ---
    mid = len(arr) // 2
    
    # Allocating new memory blocks for the halves (The O(n) memory tax)
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively tear down the left and right sides
    merge_sort(left_half)
    merge_sort(right_half)

    # --- PHASE 2: THE MERGE ---
    # We only reach this point when left_half and right_half are fully sorted
    i = 0  # Pointer for left_half
    j = 0  # Pointer for right_half
    k = 0  # Pointer for the main arr

    # Compare elements and stitch them back together in order
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Edge Case Shield: Pick up the leftovers
    # If one half was longer, dump the remaining elements into the main array
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

#Runtime Input
n = int(input("Enter number of Elements:"))
arr = list(map(int,input("Enter Elements:").split()))
print("Before Sorting:",arr)
print("After Sorting:",merge_sort(arr))
