def is_prime(n,divisor=2):
    if n<=1:
        return False
    if divisor *divisor>n:
        return True
    if n%divisor==0:
        return False
    return is_prime(n,divisor+1)
number =int(input())
if is_prime(number):
    print("it is a prime number")
else:
    print("it is not a prime number")
