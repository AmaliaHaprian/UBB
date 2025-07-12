import random
import math
import timeit
from audioop import reverse

from texttable import Texttable

# --- Functions that implement program requirements

def generate_list(user_int, random_list)-> list:
    for i in range(user_int):
        random_list.append(random.randint(0,1000))
    return random_list

#T(n)=2*n^(1/2) =>O(n^(1/2))
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

    # If element is found
    if search_list[int(prev)] == x:
        return prev

    return -1

"""
The best case of jump search is when the first element of the array is the element
we are searching for, as only one comparison is required. The time complexity in this 
case is O(1).
Worst case occurs when the value we are searching for is in the last block of the array.
In this case, there will be n^(1/2) jumps and n^(1/2)+n^(1/2)-1 comparisons.
The average case time complexity is O(n^(1/2)).
"""

# T(n)=1 +2 + ... + (n-1)=(n-1)(n)/2 =>O(n^2)
def insert_sort(unsorted_list: list) ->list:
    for i in range(1, len(unsorted_list)): #O(n)
        aux=unsorted_list[i]
        j=i-1
        while j>=0 and unsorted_list[j]>aux:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1]=aux

    return unsorted_list

"""
For insert sort, the worst-case time complexity happens when the list of numbers is in reverse order
because for each element of the list, the algorithm has to compare it to all of the elements before
and move each one of it one position to the right, shifting the entire sorted sublist. The time 
complexity is O(n^2).
The best-case time complexity happens when the list is already sorted. In this case
the current element is only compared with the right-mose element of the sorted sublist. The time complexity
is O(n).
The average time complexity is also O(n^2), although the exact number of comparisons
and swaps may vary depending on the length of the list.
"""


def shell_sort(unsorted_list: list) ->list:
    interval = len(unsorted_list) // 2
    while interval > 0: # n/2+ n/4+ n/8+....
        for i in range(interval, len(unsorted_list)): # n/2+n/4+...
            aux = unsorted_list[i]
            j = i
            while j >= interval and unsorted_list[j - interval] > aux:
                unsorted_list[j] = unsorted_list[j - interval]
                j = j- interval
            unsorted_list[j] = aux

        interval = interval // 2
    return unsorted_list

"""
For shell sort, the worst-case complexity happens when the list is reversed and it is O(n^2).
The best case complexity occurs when the list is already sorted and the time complexity is 
O(n*log(n)).
The average case complexity occurs when the elements are in a random order, neither ascending nor
descending. The time complexity is O(n*log(n)).
"""

# --- Functions that help implement the code

def reverse_list(unsorted_list):
    for i in range (0, len(unsorted_list)-1):
        for j in range(0, len(unsorted_list)-i-1):
            if unsorted_list[j]<unsorted_list[j+1]:
                aux=unsorted_list[j]
                unsorted_list[j]=unsorted_list[j+1]
                unsorted_list[j+1]=aux
    return unsorted_list

def generate_list_of_lists(list_of_lists):
    first=500
    for i in range(5):
        small_list=[]
        generate_list(first, small_list)
        list_of_lists.append(small_list)
        first=first*2
    return list_of_lists

def build_table(list_of_lists, type_case):
    copy_list=[]
    table = Texttable()
    table.add_row(['Nr', 'List length', 'Jump Search', 'Insert Sort', 'Shell Sort'])
    for i in range(len(list_of_lists)):
        copy_list.append(list_of_lists[i])

        start_is=timeit.default_timer()*1000
        row=insert_sort(list_of_lists[i])
        end_is=timeit.default_timer()*1000

        reverse_list(copy_list[i])
        start_ss=timeit.default_timer()*1000
        row=shell_sort(copy_list)
        end_ss=timeit.default_timer()*1000

        #insert_sort(list_of_lists[i])
        if type_case==6:
            x=-1
        elif type_case==7:
            x=random.randint(0,len(list_of_lists[i]))
        elif type_case==8:
            x=0

        start_js = timeit.default_timer()*1000
        row = jump_search(list_of_lists[i], list_of_lists[i][x])
        end_js = timeit.default_timer()*1000

        table.add_row([i, len(list_of_lists[i]), end_js-start_js, end_is-start_is, end_ss-start_ss])
    return table

# --- User interface functions

def get_number(number_list: list):
    x = int(input("Enter the number you are searching for:"))
    if jump_search(number_list, x)>=0:
        print("The number", x, "is in the list on position", jump_search(number_list, x))
    else:
        print("The number", x, "is not in the list")

def print_list(new_list):
    print("You have chosen to generate a list!")
    n = int(input("Enter the length of the list: "))
    generate_list(n, new_list)
    print("The list is", new_list)
    print("Please continue with other options:")

def start():
    first_entry = True
    sort_chosen = False
    number_list = []
    while True:

        print("       ---Menu---")
        print("  1.Generate list")
        print("  2.Jump Search")
        print("  3.Insert sort")
        print("  4.Shell sort")
        print("  5.Exit")
        print("  6.Worst case")
        print("  7.Average case")
        print("  8.Best case")
        print(" ")

        choice=input("Enter your choice: ").strip()

        if choice=="1":
            if first_entry==False:
                number_list=[]
            first_entry=False
            print_list(number_list)

        elif choice=="2":
            if first_entry:
                print("You have to generate a list first. Try again!")
            elif sort_chosen==False:
                print("For jump search the list has to be sorted. Please choose a sorting method first!")
            else:
                print("You have chosen to search for an element!")
                get_number(number_list)

        elif choice=="3":
            if first_entry:
                print("You have to generate a list first! Try again!")
            elif sort_chosen==False:
                sort_chosen = True
                insert_sort(number_list)
            elif sort_chosen==True:
                print("The list is already sorted! Proceed with other options")
                sort_chosen = False

        elif choice=="4":
            if first_entry:
                print("You have to generate a list first! Try again!")
            elif sort_chosen==False:
                sort_chosen = True
                shell_sort(number_list)
            elif sort_chosen==True:
                sort_chosen = False

        elif choice=="5":
            print("Thank you for using this program!")
            break

        elif "6" <= choice <= "8":
            list_of_lists=[]
            generate_list_of_lists(list_of_lists)
            initial_copy=list_of_lists[:]

            if choice=="6":
                print("You have chosen to see the worst case complexity")
                type_case=6
                for i in range(len(list_of_lists)):
                    reverse_list(list_of_lists[i])
                print("The worst case time (in milliseconds) is:")
                print(build_table(list_of_lists, type_case).draw())

            elif choice=="7":
                print("You have chosen to see the average case complexity")
                type_case = 7
                print("The average case time (in milliseconds) is:")
                print(build_table(initial_copy, type_case).draw())

            elif choice=="8":
                print("You have chosen to see the best case complexity")
                type_case = 8
                for i in range(len(list_of_lists)):
                    insert_sort(list_of_lists[i])
                print("The best case time (in milliseconds) is:")
                print(build_table(list_of_lists, type_case).draw())

        else:
            print("Please choose a valid option!")

start()