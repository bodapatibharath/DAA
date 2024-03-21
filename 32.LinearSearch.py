def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1
my_list = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
target_value = int(input("Enter the value to search for: "))

index = linear_search(my_list, target_value)

if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found in the list.")
