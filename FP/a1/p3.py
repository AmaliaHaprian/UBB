# Solve the problem from the third set here
def is_prime(n: int) -> bool:    #the function checks if a number is prime or not
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3, n//2+1,2):
        if n % i == 0:
            return False
    return True

def is_div(n: int, d: int) -> bool: #the function checks if two numbers are divisible
    if n%d==0:
        return True
    return False

def get_number(n: int): #the function counts the elements of a sequence in which composed numbers
    cnt=1  #are replaced with their prime divisors, each divisor d being written d times
    i=2
    found=1
    while cnt<n:
        if is_prime(i):  #if the number is prime then the desired output will be said number
            found = i    #and the function only counts it one
            cnt = cnt + 1
        else:            #if the number is not prime then the function gets its prime divisors d and
            for d in range (2, i//2+1 ):       #counts them d times
                if is_div(i, d) and is_prime(d):
                    found = d
                    cnt = cnt + d
                    if cnt>=n:
                        break
        i=i+1
    return found

n= int(input("Enter a number:n= "))
print("The", n, "-th element of the sequence is", get_number(n))