def find_min_max(numbers):
    """
    Find the minimum and maximum values from a list of numbers.
    
    Args:
    numbers (list): The list of numbers.
    
    Returns:
    None
    """
    if len(numbers) == 0:
        print("The list is empty")
    else:
        min_value = min(numbers)
        max_value = max(numbers)
        print("Minimum value:", min_value)
        print("Maximum value:", max_value)

input_str = input("Enter list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]
find_min_max(numbers)
