def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
target = 17
result = binary_search(arr, target)
if result != -1:
    print("Element", target, "is present at index", result)
else:
    print("Element", target, "is not present in the array.")
