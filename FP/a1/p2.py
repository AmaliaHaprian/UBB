# Solve the problem from the second set here
n=int(input("Enter a number: "))

def fibonacci_number(n: int): #the function implements the Fibonacci sequence until
    a = 0                     #it finds the smalles number larger than the input number
    b = 1
    m=0
    while m<n:
        m=a+b
        a=b
        b=m
    return m

print("The smallest number from the Fibonacci sequence larger than", n, "is", fibonacci_number(n))