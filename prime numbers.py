def is_prime(num,divisor=2):
    if num<2:
        return False
    if divisor*divisor>num:
        return True
    if num%divisor ==0:
        return False
    return is_prime(num,divisor+1)
def print_primes(start,end):
    if start>end:
        return
    if is_prime(start):
        print(start,end=' ')
    print_primes(start+1,end)
print_primes(1,50)
