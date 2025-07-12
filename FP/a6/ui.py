#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from functions import *

def print_menu():
    print("""
    ---Add a transaction 
        add <value> <type> <description>
        insert <day> <value> <type> <description>
    ---Modify a transaction
        remove <day>
        remove <start day> to <end day>
        remove <type>
        replace <day> <type> <description> with <value>
    ---Display transactions having certain properties
        list
        list <type>
        list [ < | = | > ] <value>
        list balance <day>
    ---Filter
        filter <type>
        filter <type> <value>
    ---Undo
        undo
        """)

def get_input(list_of_transactions):
    list_of_transactions=generate_transactions()
    list_of_transactions.sort(key=lambda x: x['day'])
    history=[]
    history.append(copy.deepcopy(list_of_transactions))

    while True:
        print_menu()
        answer=input("What would you like to do?")

        processed_answer=process_answer(answer)
        if len(processed_answer)<=0:
            print("Please input a command")
        elif len(processed_answer)>6:
            print("Error! Too many parameters")
        else:
            if processed_answer[0]=='add':
                try:
                    if len(processed_answer)==4:
                        list_of_transactions=add_transaction(history,list_of_transactions, processed_answer[1],processed_answer[2],processed_answer[3])
                    else:
                        print("Error! Not enough parameters")
                except TypeError as te:
                    print(te)

            elif processed_answer[0]=='insert':
                try:
                    if len(processed_answer)==5:
                        list_of_transactions=insert_transaction(history,list_of_transactions,processed_answer[1],processed_answer[2],processed_answer[3],processed_answer[4])
                    else:
                        print("Error! Not enough parameters")
                except ValueError as ve:
                    print(ve
            elif processed_answer[0]=='remove':
                if len(processed_answer) == 2:
                    if processed_answer[1]=='in' or processed_answer[1]=='out':
                        list_of_transactions = remove_type(history,list_of_transactions, processed_answer[1])
                    else:
                        try:
                            processed_answer[1] = int(processed_answer[1])
                            list_of_transactions=remove_day(history,list_of_transactions, processed_answer[1])
                        except ValueError:
                            print('Error! There should be an integer for the day specified')

                elif len(processed_answer)==4:
                    list_of_transactions=remove_from_to(history,list_of_transactions, processed_answer[1], processed_answer[3])
                else:
                    print("Error! Wrong input. Try again!")
            elif processed_answer[0] == 'replace':
                try:
                    processed_answer[1] = int(processed_answer[1])
                    if find_is_transaction(list_of_transactions,processed_answer[1],processed_answer[2], processed_answer[3]):
                        list_of_transactions=modify_value(history,list_of_transactions,processed_answer[1],processed_answer[5],processed_answer[2],processed_answer[3])

                    else:
                        print('There is no transaction with the data specified')
                except ValueError:
                    print('Error! There should be an integer for the day specified')

            elif processed_answer[0]=='list':
                if len(processed_answer) == 1:
                    display_list(list_of_transactions)

                elif len(processed_answer) == 2:
                    if processed_answer[1] == 'in' or processed_answer[1] == 'out':
                        list_type(list_of_transactions, processed_answer[1])
                    else:
                        print('Error! Type should be in or out')

                elif len(processed_answer) == 3:
                    if processed_answer[1]=='balance':
                        try:
                            processed_answer[2] = int(processed_answer[2])
                            if find_is_day(list_of_transactions, processed_answer[2]):
                                print('The balance on day', processed_answer[2], 'is', calculate_balance(list_of_transactions, processed_answer[2]))
                            else:
                                print("There is no transaction on day", processed_answer[2])
                        except ValueError:
                            print('Error! There should be an integer for the day specified')

                    elif processed_answer[1] == '>'or processed_answer[1] == '<' or processed_answer[1] == '=':
                        list_quantity(list_of_transactions, processed_answer[1], processed_answer[2])
                    else:
                        print("Error! Please use of the required commands")
                else:
                    print("Error! Too many parameters")
            elif processed_answer[0] =='filter':
                if len(processed_answer) >3:
                    print("Error! Too many parameters")
                else:
                    if processed_answer[1]=='in' or processed_answer[1]=='out':

                        if len(processed_answer) == 2:
                            filter_type(history,list_of_transactions, processed_answer[1])
                            display_list(list_of_transactions)

                        elif len(processed_answer) == 3:
                            try:
                                processed_answer[2] = int(processed_answer[2])
                            except ValueError:
                                print('Error! There should be an integer for value')
                            else:
                                filter_type_value(history,list_of_transactions, processed_answer[1], processed_answer[2])
                                display_list(list_of_transactions)
                    else:
                        print('Error! Type should be in or out')

            elif processed_answer[0] == 'undo':
                if len(processed_answer) >1:
                    print("Error! Too many parameters")
                else:
                    try:
                        list_of_transactions=undo_operation(history)

                    except IndexError:
                        print("Error! There is nothing to undo anymore!")
            else:
                print("Syntax error. Please use one of the required commands")

# (C)- list
def display_list(list_of_transactions):
    print(build_table(list_of_transactions).draw())

def list_type(list_of_transactions,type):
    print(build_table_type(list_of_transactions,type).draw())

def list_quantity(list_of_transactions, quantifier,value_to_compare):
    try:
        value_to_compare = int(value_to_compare)
    except ValueError:
        print('Error! Value should be an integer')
    else:
        print(build_table_quantifier(list_of_transactions,quantifier,value_to_compare).draw())
