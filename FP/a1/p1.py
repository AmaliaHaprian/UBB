# Solve the problem from the first set here
def get_digits(n: int): #the function creates a sorted list of all the digits of n
    m = 0               #and returns the minimal number formed with the same digits
    list = []
    while n!=0:
        list.append(n%10)
        n=n//10
    list.sort()
    for i in range(len(list)):
        m = m * 10 + list[i]
    return m

n=int(input("Enter a number="))
print("The minimal number formed with the same digits of", n, "is", get_digits(n))