def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    unsorted_list = input("Enter the unsorted list separated by spaces: ")
    unsorted_list = list(map(int, unsorted_list.split()))
    result = bubble_sort(unsorted_list)
    print(result)
