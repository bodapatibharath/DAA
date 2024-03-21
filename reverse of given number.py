def reverse_number(number):
    if number == 0:
        return 0
    else:
        return (number % 10) * 10 ** (len(str(number)) - 1) + reverse_number(number // 10)


original_number = int(input())
reversed_number = reverse_number(original_number)
print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_number}")
