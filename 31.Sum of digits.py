def sum_of_digits(number):
    digit_sum = 0
    for digit_char in str(number):
        digit = int(digit_char)
        digit_sum += digit
    return digit_sum
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
