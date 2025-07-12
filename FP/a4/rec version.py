"""
7. Generate all subsequences of length 2n+1, formed only by 0, -1 or 1,
such that a1 = 0, ..., a2n+1= 0 and |ai+1 - ai| = 1 or 2, for any 1 ≤ i ≤ 2n.
"""
# --- Function that help implement the code ---
def solution(seq):
    if seq[0]==0 and seq[-1]==0:
        return True
    else:
        return False

def is_safe(prev:int, current:int):
    if abs(prev-current)==1 or abs(prev-current)==2:
        return 1
    else:
        return 0

# --- Recursive method ---

# 0(n)=3^(2*n+1) -- for each of the 2*n+1 position that have to be filled in, there are 3 possible choices
def back_recursive(l, sequence, n):
    if l==2*n+1:
        if solution(sequence):
            print(sequence)
    else:
        for j in [0, -1, 1]:
            if is_safe(sequence[-1], j):
                sequence.append(j)
                back_recursive(l+1, sequence, n)
                sequence.pop()

# --- Iterative method ---
def back_it(n):
    s = [(1, [0])]
    while s:
        l, seq = s.pop()
        if l == 2 * n + 1:
            if solution(seq):
                print(seq)
        else:
            for j in [0, -1, 1]:
                if is_safe(seq[-1],j):
                    s.append((l+1, seq+[j]))

"""
7. Given a set of integers A, determine if it can be partitioned into two subsets with equal sum. For example, set A = { 1, 1, 1, 1, 2, 3, 5 } 
can be partitioned into sets A1 = { 1, 1, 2, 3 } and A2 = { 1, 1, 5 }, each of them having sum 7. Display one such possibility.
"""
# ---Naive implementation ---
def is_sum(n,sum,initial_set,subset1):
    if n==0:
        print("False")
        return False
    if n==0 and sum!=0:
        print("False")
        return False
    if sum==0:
        subset1.reverse()
        subset2=initial_set.copy()
        for i in subset1:
            subset2.remove(i)
        print("True. A possible pair of sets is:")
        print("Elements of set 1:", subset1)
        print("Elements of set 2:", subset2)
        return True

    if initial_set[n-1]>sum:
        return is_sum(n-1,sum,initial_set,subset1)

    return is_sum(n-1,sum,initial_set,subset1) or is_sum(n-1, sum-initial_set[n-1], initial_set, subset1+[initial_set[n-1]])

# ---Dynamic programming ---
def dp_vs(n,sum, initial_set):
    dp=[[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,sum+1):
            if j==0:
                dp[i][j]=True
            if i==0:
                dp[i][j]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if initial_set[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                include=dp[i-1][j-initial_set[i-1]]
                exclude=dp[i-1][j]

                dp[i][j]= include or exclude
    #return dp[n][sum]
    if dp[n][sum]==False:
        print("False")
    else:
        set1=[]
        set2=[]
        i=n
        current_sum=sum
        while (i>0 and current_sum>=0):
            if dp[i-1][current_sum]:
                i = i-1
                set2.append(initial_set[i])

            else:
                i = i - 1
                current_sum = current_sum - initial_set[i]
                set1.append(initial_set[i])
        set1.reverse()
        set2.reverse()
        print("True. A possible pair of sets is:")
        print("Elements of set 1:",set1)
        print("Elements of set 2:",set2)


def start():
    #n=int(input("Enter number:"))
    #print("Iterative version:")
    #back_it(n)
    #print(" ")
    #print("Recursive version:")
    #back_recursive(1, [0], n)

    print("Enter the way you want to solve this problem:")
    print("1. Naive implementation")
    print("2. Dynamic programming")
    choice=int(input("Your choice is:"))

    initial_set = []
    sum = 0
    n = int(input("Enter the cardinal of the set:"))
    print("Enter the elements of the list")
    for i in range(n):
        element = int(input())
        initial_set.append(element)
        sum = sum + element
    if sum % 2 == 1:
        print("the set cannot be partitioned into two subsets with equal sum")
    else:
        if choice==1:
            is_sum(n, sum // 2, initial_set, [])

        elif choice==2:
            dp_vs(n, sum // 2, initial_set)
        else:
            print("Choose a valid option")

start()
