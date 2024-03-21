def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
term = int(input())
if term<=0:
    print("enter positive integers")
else:
    print("fibonacci series :")
    for i in range (term):
        print (fibonacci(i),end=" ")
        
