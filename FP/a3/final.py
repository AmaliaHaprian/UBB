import random
import math
import timeit

from texttable import Texttable

# --- Functions that implement program requirements

def generate_list(user_int, random_list)-> list:
    for i in range(user_int):
        random_list.append(random.randint(0,1000))
    return random_list

def jump_search(search_list: list, x: int):
    pos=0
    length=len(search_list)
    jump=int(math.sqrt(length))
    for i in range(0, length, jump):
        if search_list[i] < x:
            pos=i
        elif search_list[i]==x:
            return i
        else:
            return -1
    for j in range(pos, pos+jump):
        if search_list[j] == x:
            return j
    return -1

def insert_sort(unsorted_list: list) ->list:
    for i in range(1, len(unsorted_list)):
        aux=unsorted_list[i]
        j=i-1
        while j>=0 and unsorted_list[j]>aux:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1]=aux

    return unsorted_list

def shell_sort(unsorted_list: list) ->list:
    interval = len(unsorted_list) // 2
    while interval > 0:
        for i in range(interval, len(unsorted_list)):
            aux = unsorted_list[i]
            j = i
            while j >= interval and unsorted_list[j - interval] > aux:
                unsorted_list[j] = unsorted_list[j - interval]
                j = j- interval
            unsorted_list[j] = aux

        interval = interval // 2
    return unsorted_list

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
    starting_length=int(input("Enter the starting length: "))
    for i in range(5):
        small_list=[]
        generate_list(starting_length, small_list)
        list_of_lists.append(small_list)
        starting_length=starting_length*2
    return list_of_lists

def build_table(list_of_lists, type_case):
    table = Texttable()
    table.add_row(['Nr','List length', 'Insert Sort', 'Shell Sort'])
    for i in range(len(list_of_lists)):
        copy_list=list_of_lists[i]

        start_is=timeit.default_timer()
        row=insert_sort(list_of_lists[i])
        end_is=timeit.default_timer()

        if type_case==6:
             reverse_list(list_of_lists[i])

        start_ss=timeit.default_timer()
        row=shell_sort(list_of_lists[i])
        end_ss=timeit.default_timer()

        table.add_row([i, len(list_of_lists[i]), end_is-start_is, end_ss-start_ss])
    return table

# --- User interface functions

def get_number(number_list: list):
    x = int(input("Enter the number you are searching for:"))
    if jump_search(number_list, x)>=0:
        print("The number", x, "is in the list on position", jump_search(number_list, x))
    else:
        print("The number", x, "is not in the list")

def print_list(new_list) -> None:
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
        print("  7.Best case")
        print("  8.Average case")
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
                type_case=6
                for i in range(len(list_of_lists)):
                    reverse_list(list_of_lists[i])
                print("The worst case sorting time is:")
                print(build_table(list_of_lists,type_case).draw())

            elif choice=="7":
                type_case=7
                for i in range(len(list_of_lists)):
                    insert_sort(list_of_lists[i])
                print("The best case sorting time is:")
                print(build_table(list_of_lists,type_case).draw())

            elif choice=="8":
                type_case=8
                print("The average case sorting time is:")
                print(build_table(initial_copy,type_case).draw())
        else:
            print("Please choose a valid option!")

start()