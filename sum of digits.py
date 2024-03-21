def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10 
        total += digit
        number //= 10
    return total

num = int(input("Enter a positive integer: "))
result = sum_of_digits(num)
print(f"Sum of digits of {num} is {result}.")
