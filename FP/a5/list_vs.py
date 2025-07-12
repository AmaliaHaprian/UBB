from random import randint
#
# Write the implementation for A5 in this file
#

#
# Write below this comment
# Functions to deal with complex numbers -- list and dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def get_real(nr):
    return nr[0]
    #return nr["real_part"]

def get_imaginary(nr):
    return nr[1]
    #return nr["imaginary_part"]

def set_real(nr,new_real):
    nr[0] = new_real
    #nr["real_part"]=new_real

def set_imaginary(nr,new_imaginary):
    nr[1] = new_imaginary
    #nr["imaginary_part"] = new_imaginary

#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def nr_of_different_elements(l):
    single_elem_list=[]
    for i in l:
        if i not in single_elem_list:
            single_elem_list.append(i)
    return len(single_elem_list)

def naive_pb(l):
    max_subarray=[]
    for i in range(len(l)):
        subarray=[l[i]]
        for j in range(i+1,len(l)):
            subarray.append(l[j])
            if nr_of_different_elements(subarray)<=3 and len(subarray)>len(max_subarray):
                max_subarray=subarray.copy()
    return max_subarray

def calculate_modulus(nr):
    return (get_real(nr)**2)+(get_imaginary(nr)**2)

def dp_pb(l):
    max_length=1
    best_end=0

    indices_array=[1]
    previous_indices=[-1]
    for i in range(1, len(l)):
        indices_array.append(1)
        previous_indices.append(-1)
        for j in range(i-1,-1,-1):
            if indices_array[j]+1> indices_array[i] and calculate_modulus(l[j]) < calculate_modulus(l[i]):
                indices_array[i]=indices_array[j]+1
                previous_indices[i]=j
        if indices_array[i]> max_length:
            best_end=i
            max_length= indices_array[i]

    solution=[l[best_end]]
    while previous_indices[best_end]!=-1:
        solution.append(l[previous_indices[best_end]])
        best_end=previous_indices[best_end]
    solution.reverse()
    return solution
#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def read_numbers_ui(numbers):
    n = int(input("How many numbers do you want to add: "))
    for i in range(n):

        try:
            real=input("Real part of the number: ")
            imaginary=input("Imaginary part of the number: ")
            nr=create_number(real, imaginary)
            numbers.append(nr)
        except ValueError as ve:
            print(ve)

    return numbers

def display_list(number_list):
    for number in number_list:
        print(to_str(number))

def print_naive_pb(l):
    print("Determine the length and the elements of a longest subarray of numbers that contain at most 3 distinct values.")
    print("The length of the subarray is:", len(l))
    print("The subarray is:")
    display_list(l)

def print_dp_pb(l):
    print("Determine the length and the elements of a longest increasing subsequence, when considering each number's modulus.")
    print("The length of the subarray is:", len(l))
    print("The subarray is:")
    display_list(l)

def print_menu():
    print("Choose an option from the menu:")
    print("1.Read numbers")
    print("2.Display the list of number")
    print("3.Solve problems")
    print("4.Exit")
    print(" ")

def start():
    numbers=generate_random_numbers(10)
    while True:
        try:
            print_menu()
            choice=int(input("Enter your choice: "))

            if choice==1:
                read_numbers_ui(numbers)

            elif choice==2:
                display_list(numbers)

            elif choice==3:
                print_naive_pb(naive_pb(numbers))
                print_dp_pb(dp_pb(numbers))

            elif choice==4:
                return

            else:
                print("Choose a valid option")
        except ValueError as ve:
            print(ve)

def create_number(real, imaginary):
    if real!=int(real) or imaginary!=int(imaginary):
           raise ValueError('Real and Imaginary values must be integers.')
    if -100>real or real>100 or imaginary<-100 or imaginary>100:
        raise ValueError('Real and Imaginary values must be between -100 and 100 but were given as ' + str(real) + ' and ' + str(imaginary)+'.Try again!')

    return [real, imaginary]
    #return {"real_part": real, "imaginary_part": imaginary}

# --- Functions for numbers ---

def to_str(nr):
    return "Nr= " + str(get_real(nr)) + " + " + str(get_imaginary(nr)) + " i"


def generate_random_numbers(n):
    number_list=[]
    for i in range(n):
        real=randint(-100,100)
        imaginary=randint(-100,100)
        number_list.append(create_number(real,imaginary))

    return number_list

# --- Testing ---
def test_nr():
    nr=create_number(5,6)
    assert get_real(nr)==5
    assert get_imaginary(nr)==6


test_nr()

start()
