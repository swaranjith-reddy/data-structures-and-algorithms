def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1: ]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return QuickSort(left) + [pivot] + QuickSort(right)

n = int(input("Enter number of Elements:"))
arr = list(map(int,input("Enter Elements:").split()))
print("Before Sorting:",arr)
print("After Sorting:",QuickSort(arr))
