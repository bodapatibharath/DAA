def is_perfect_number_filter_method(number):
    divisors = list(filter(lambda x: number % x == 0, range(1, number)))
    return sum(divisors) == number


input_number = int(input())
if is_perfect_number_filter_method(input_number):
    print(f"The number {input_number} is a perfect number.")
else:
    print(f"The number {input_number} is not a perfect number.")
