# ---Naive implementation---
def find_partition(current_elem,current_sum):
    if current_elem==0 and current_sum!=0:
        return False
    elif sum==0:
        return True


# ---Dynamic Programming---
def dp_vs(n,sum, initial_set):
    dp=[[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(0,sum+1):
        for j in range(0,n+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True

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
        dp_vs(n,sum//2, initial_set)
    #        print(dp_vs(n,sum//2,initial_set,dp))
     #       find_sets(n,sum//2,initial_set,dp)
      #  else:
       #     print(dp_vs(n, sum // 2, initial_set, dp))

start()
