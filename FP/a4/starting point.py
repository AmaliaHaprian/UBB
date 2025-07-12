def is_sum(n,sum,initial_set,subset1):
    if n==0 and sum!=0:
        return False
    if sum==0:
        subset1.reverse()
        subset2=initial_set.copy()
        for i in subset1:
            subset2.remove(i)
        print("Elements of set 1:", subset1)
        print("Elements of set 2:", subset2)
        return True

    if initial_set[n-1]>sum:
        return is_sum(n-1,sum,initial_set,subset1)

    return is_sum(n-1,sum,initial_set,subset1) or is_sum(n-1, sum-initial_set[n-1], initial_set, subset1+[initial_set[n-1]])

def start():
    initial_set=[]
    sum=0
    n=int(input("Enter the cardinal of the set:"))
    print("Enter the elements of the list")
    for i in range(n):
        element=int(input())
        initial_set.append(element)
        sum=sum+element
    if sum%2==1:
        print("the set cannot be partitioned into two subsets with equal sum")
    else:
        is_sum(n,sum//2,initial_set,[])

start()