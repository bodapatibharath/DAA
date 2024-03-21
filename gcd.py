def gcd_recursive(a,b):
    if b==0:
        return a
    else:
        return gcd_recursive(b,a%b)
num1=int(input())
num2=int(input())
result = gcd_recursive(num1,num2)
print (f"the gcd of {num1} and {num2} is {result}")
