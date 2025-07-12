import random
import math

# --- Functions that implement program requirements

def generate_list(user_int, random_list)-> list:
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

    # If element is found
    if search_list[int(prev)] == x:
        return prev

    return -1

def insert_sort(unsorted_list: list, step: int) ->list:
    step_counter=0
    for i in range(1, len(unsorted_list)):
        aux=unsorted_list[i]
        j=i-1
        while j>=0 and unsorted_list[j]>aux:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1]=aux
        step_counter = step_counter + 1

        if step!=0:
            if step_counter % step == 0:
                print_iteration(unsorted_list, step_counter)
    return unsorted_list

def shell_sort(unsorted_list: list, step: int) ->list:
    step_counter = 0
    interval = len(unsorted_list) // 2
    while interval > 0:
        for i in range(interval, len(unsorted_list)):
            aux = unsorted_list[i]
            j = i
            while j >= interval and unsorted_list[j - interval] > aux:
                unsorted_list[j] = unsorted_list[j - interval]
                j = j- interval
            unsorted_list[j] = aux
            step_counter = step_counter + 1

            if step != 0:
                if step_counter % step == 0:
                    print_iteration(unsorted_list, step_counter)

        interval = interval // 2
    return unsorted_list

# --- User interface functions

def print_iteration(temp_list,step_counter):
    if step_counter==1:
        print("After 1 operation the list is:", temp_list)
    else:
        print("After", step_counter, "operations the list is:", temp_list)

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
        print(" ")

        choice=input("Enter your choice: ").strip()

        if choice=="1":
            if first_entry==False:
                number_list=[]
                sort_chosen = False
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
            else:
                if sort_chosen==False:
                    sort_chosen = True
                    print("You have chosen insert sort!")
                    step = int(input("Enter the step you want to see the changes in the list:"))
                    print("The sorted list is:", insert_sort(number_list, step) )
                    print(" ")
                else:
                    print("The list is already sorted! Proceed with other options")

        elif choice=="4":
            if first_entry:
                print("You have to generate a list first! Try again!")
            else:
                if sort_chosen==False:
                    sort_chosen==False
                    sort_chosen = True
                    print("You have chosen shell sort!")
                    step = int(input("Enter the step you want to see the changes in the lists:"))
                    print("The sorted list is:", shell_sort(number_list, step))
                    print(" ")
                else:
                    print("The list is already sorted! Proceed with other options")

        elif choice=="5":
            print("Thank you for using this program!")
            break

        else:
            print("Please choose a valid option!")

start()