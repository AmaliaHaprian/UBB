import random
import math
import timeit

def generate_list(user_int, random_list):
    for i in range(user_int):
        random_list.append(random.randint(0,1000))
    return random_list


def jump_search(search_list: list, x: int):
    # Finding block size to be jumped
    step = int(math.sqrt(len(search_list)))

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while search_list[int(min(step, len(search_list)) - 1)] < x:
        prev = step
        step += int(math.sqrt(len(search_list)))
        if prev >= len(search_list):
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while search_list[int(prev)] < x:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, len(search_list)):
            return -1
    if search_list[int(prev)] == x:
        return prev

    return -1

def insert_sort(unsorted_list: list) ->list:
    for i in range(1, len(unsorted_list)): #O(n)
        aux=unsorted_list[i]
        j=i-1
        while j>=0 and unsorted_list[j]>aux:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1]=aux

    return unsorted_list

def start():
    n = int(input("Enter the number of elements: "))
    for i in range(6):
        number_list=[]
        generate_list(n,number_list)
        print(number_list)
        #print(number_list[-1])
        #print(len(number_list))

        insert_sort(number_list)

        start1=timeit.default_timer()*1000
        jump_search(number_list,number_list[-1])
        end1=timeit.default_timer()*1000
        print(jump_search(number_list,number_list[-1]))
        #if jump_search(number_list,number_list[len(number_list)-1]) >=0:
         #   print("found")

        start2 = timeit.default_timer() * 1000
        jump_search(number_list, number_list[0])
        end2 = timeit.default_timer() * 1000
        #print(jump_search(number_list, number_list[0]))
        #if jump_search(number_list,number_list[len(number_list)-1]) >=0:
          #  print("found")

       # x=random.randint(0,len(number_list))
        #start3 = timeit.default_timer() * 1000
       # jump_search(number_list, number_list[x])
       # end3 = timeit.default_timer() * 1000
        #print(jump_search(number_list, number_list[x]))
        #if jump_search(number_list,number_list[len(number_list)-1]) >= "0":
         #   print("found")
        print("n=", n)
        n=n*2

        print("iteration", i)
        #print(end1-start1)
        #print(end2 - start2)
        #print(end3 - start3)
        print(" ")

start()
