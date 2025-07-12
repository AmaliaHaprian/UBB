#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

from random import randint,choice
import copy
from texttable import Texttable
from pdoc import pdoc

def set_day(transaction,day):
    """
    Sets a new value to the day of a transaction
    :param transaction: a certain transaction
    :param day: the new value for day
    :return: the modified transaction
    """
    transaction['day']=day
    return transaction

def set_value(transaction,value):
    """
    Sets a new value to the value of a transaction
    :param transaction: a  certain transaction
    :param value: the new value of the transaction
    :return: the modified transaction
    """
    transaction['value']=value
    return transaction

def set_type(transaction,type):
    """
    Sets a new value to the type of the transaction
    :param transaction: a  certain transaction
    :param type: the new value of the type of the transaction
    :return: the modified transaction
    """
    transaction['type']=type
    return transaction

def set_description(transaction,description):
    """
    Sets a new value to the description of the transaction
    :param transaction: a  certain transaction
    :param description: the new value of the description of the transaction
    :return: the modified transaction
    """
    transaction['description']=description
    return transaction

def get_day(transaction):
    """

    :param transaction: a certain transaction
    :return: the day of the transaction
    """
    return transaction['day']

def get_value(transaction):
    """

    :param transaction: a certain transaction
    :return: the value of the transaction
    """
    return transaction['value']

def get_type(transaction):
    """

    :param transaction: a certain transaction
    :return: the type of the transaction
    """
    return transaction['type']

def get_description(transaction):
    """

    :param transaction: a certain transaction
    :return: the description of the transaction
    """
    return transaction['description']

# (A)- add

def add_transaction(history,list_of_transactions, value, type, description):
    """
    The function add a new transaction on the current day, also handling the exception that might occur from wrong input data
    :param history: list that contains all the changes made to the list of transactions so far
    :param list_of_transactions: list of all transactions
    :param value: the value of transaction
    :param type: the type of transaction: either 'in' or 'out'
    :param description: the description of the transaction
    :return: the modified list of transactions, with the new transaction
    """

    try:
        value = int(value)

    except:
        raise TypeError('Error!Value must be an integer')
    else:
        if type=='in' or type=='out':
            current_day = list_of_transactions[-1]['day']
            transaction = {'day': current_day, 'value': value, 'type': type, 'description': description}
            list_of_transactions.append(transaction)
            history.append(copy.deepcopy(list_of_transactions))
            return list_of_transactions
        else:
            print("Error! Type should be either 'in' or 'out'")

def insert_transaction(history,list_of_transactions, day, value, type, description):
    """
    The function inserts a new transaction, taking into account the day, so that it is in increasing order
    :param history:list that contains all the changes made to the list of transactions so far
    :param list_of_transactions:list of all transactions
    :param day: the day of transaction
    :param value:the value of transaction
    :param type:the type of transaction: either 'in' or 'out'
    :param description:the description of the transaction
    :return: the modified list of transactions, with the new transaction at the right place in the list
    """
    try:
        day=int(day)
        value = int(value)
    except:
        raise ValueError('Error!There should be an integer for day and value')
    else:
        if type == 'in' or type == 'out':
            new_list=[]
            for transaction in list_of_transactions:
                if transaction['day']<= day:
                    new_list.append(copy.deepcopy(transaction))
            new_transaction={'day':day,'value':value,'type':type,'description':description}
            new_list.append(new_transaction)
            for transaction in list_of_transactions:
                if transaction['day']> day:
                    new_list.append(copy.deepcopy(transaction))
            history.append(copy.deepcopy(new_list))
            return new_list
        else:
            print("Error! Type should be either 'in' or 'out'")
# (B)- modify

def remove_day(history,list_of_transactions, day_to_remove):
    """
    The function takes as input a certain day of transaction and removes all the transactions that have that day
    :param history:list that contains all the changes made to the list of transactions so far
    :param list_of_transactions:list of all transactions
    :param day_to_remove: the day the user wants to remove
    :return: the modified list of transactions, without the transactions made on the day specified
    """

    new_list=[]
    for transaction in list_of_transactions:
        day=get_day(transaction)
        if not int(day)==day_to_remove:
            new_list.append(transaction)
    history.append(copy.deepcopy(list_of_transactions))
    return new_list

def remove_from_to(history,list_of_transactions, start_day, end_day):
    """
    The function takes as input a starting and ending day and removes all the transactions that have the day between the ones specified
    :param history: list that contains all the changes made to the list of transactions so far
    :param list_of_transactions: list of all transactions
    :param start_day: the starting day of transactions to be removed
    :param end_day: the ending day of transactions to be removed
    :return: the modified list, without the transactions made between the days specified
    """
    try:
        start_day=int(start_day)
        end_day=int(end_day)
    except ValueError:
        print('Error!There should be an integer for start and end day')
    else:
        for i in range(len(list_of_transactions)-1,-1,-1):
            day = get_day(list_of_transactions[i])
            if start_day <= day <= end_day:
                list_of_transactions.remove(list_of_transactions[i])
        history.append(copy.deepcopy(list_of_transactions))
        return list_of_transactions

def remove_type(history,list_of_transactions, type_to_remove):
    """
    The function takes as input a certain type of transaction and removes all the transactions that have that type
    :param history: list that contains all the changes made to the list of transactions so far
    :param list_of_transactions: list of all transactions
    :param type_to_remove: the type of transactions to be removed
    :return: the modified list, without the transactions that have the type specified
    """
    for i in range(len(list_of_transactions)-1,-1,-1):
        if list_of_transactions[i]['type']==type_to_remove:
            list_of_transactions.remove(list_of_transactions[i])
    history.append(copy.deepcopy(list_of_transactions))
    return list_of_transactions

def modify_value(history,list_of_transactions, day, new_value, type, description):
    """
    The function looks for the transaction that has the day, type and description specified, and replaces the old value with a new one
   :param history: list that contains all the changes made to the list of transactions so far
   :param list_of_transactions: list of all transactions
   :param day: the day of the transaction the user wants to modify
   :param new_value: the new value of the transaction, that will replace the old value
   :param type: the type of the transaction the user wants to modify
   :param description: the description of the transaction the user wants to modify
   :return: the modified list, with the new value of the transaction
   """
    try:
        day=int(day)
        new_value = int(new_value)
    except ValueError:
        print('Error!There should be an integer for day and value')
    else:
        for transaction in list_of_transactions:
            take_day=get_day(transaction)
            if str(take_day)==str(day) and transaction['type']==type and transaction['description']==description:
                transaction['value']=new_value
        history.append(copy.deepcopy(list_of_transactions))
        return list_of_transactions

# (D)- filter

def filter_type(history,list_of_transactions, type):
    """
    The function takes as input a certain type of transaction and keeps only the transactions that have that type
    :param history: list that contains all the changes made to the list of transactions so far
    :param list_of_transactions: list of all transactions
    :param type: the type by which to filter the transactions
    :return: the modified list, with only the transactions that have the type specified
    """
    for i in range(len(list_of_transactions)-1,-1,-1):
        if list_of_transactions[i]['type']!=type:
            list_of_transactions.remove(list_of_transactions[i])
    history.append(copy.deepcopy(list_of_transactions))
    return list_of_transactions

def filter_type_value(history,list_of_transactions, type, value):
    """
    The function takes as input a certain type and value of transaction and keeps only the transactions that have that type and a value smaller than the one specified
    :param history: list that contains all the changes made to the list of transactions so far
    :param list_of_transactions: list of all transactions
    :param type: the type by which to filter the transactions
    :param value: the value by which to filter the transactions
    :return: the modified list, with only the transactions that have the type specified and a smaller value
    """
    for i in range(len(list_of_transactions)-1,-1,-1):
        if not (list_of_transactions[i]['type']==type and list_of_transactions[i]['value']<=value):
            list_of_transactions.remove(list_of_transactions[i])
    history.append(copy.deepcopy(list_of_transactions))
    return list_of_transactions

# (E)-undo

def undo_operation(history):
    """
    The function undoes the last operation made on the list of transactions by removing it from its elements
    :param history: list that contains all the changes made to the list of transactions so far
    :return: the list of transactions before the last operation
    """
    if len(history)==1:
        history.pop()
        return []
    elif len(history)>1:
        history.pop()
        list_of_transactions=history[-1]

        return list_of_transactions
    else:
        raise IndexError

def calculate_balance(list_of_transactions,day):
    """
    The function calculates the balance of all the transactions made before or on the date specified
    :param list_of_transactions: the list of transactions
    :param day: the last day of transactions to be calculated
    :return: a number representing the sum of all transactions, some positive other negative, depending on their type
    """
    balance=0
    for i in range(len(list_of_transactions)):
        if list_of_transactions[i]['day']<=day:
            if list_of_transactions[i]['type']=='in':
                balance=balance+int(list_of_transactions[i]['value'])
            else:
                balance = balance - int(list_of_transactions[i]['value'])
    return balance

def generate_transactions():
    """
    The function generates a list of 10 random transactions
    :return: a starting list of transactions with 10 elements
    """
    list_of_transactions=[]

    type_of_transaction=["in", "out"]
    description=['salary', 'pizza', 'groceries', 'party', 'shopping']
    for i in range(10):
        transaction={
            "day":randint(1,30),
            "value":randint(1,100),
            "type": choice(type_of_transaction),
            "description":choice(description) }
        list_of_transactions.append(transaction)

    return list_of_transactions

def process_answer(answer):
    """
    The function takes the input from the user and separates it into "words", taking whitespace as a separator
    :param answer: the input from the user
    :return: a list of all the elements from the input
    """
    return answer.split()

def to_str(transaction):
    """
    The function takes the input from the user and converts it to a string
    :param transaction: a transaction made
    :return: each element associated to a key of the transaction becomes a string
    """
    day=get_day(transaction)
    value=get_value(transaction)
    type=get_type(transaction)
    description=get_description(transaction)
    transaction={'day': str(day), 'value': str(value), 'type': type, 'description': description}
    return transaction

def find_is_day(list_of_transactions, day):
    """
    The function searches if there exists a transaction on a certain day
    :param list_of_transactions: the list of transactions
    :param day: the day of the transaction the user is looking for
    :return: True if there exists a transaction on that day, False otherwise
    """
    for transaction in list_of_transactions:
        if transaction['day']==day:
            return True
    return False

def find_is_type(list_of_transactions, type):
    """
    The function searches if there exists a transaction with a certain type
    :param list_of_transactions: the list of transactions
    :param type: the type of the transaction the user is looking for
    :return: True if there exists a transaction with such type, False otherwise
    """
    for transaction in list_of_transactions:
        if transaction['type']==type:
            return True
    return False

def find_is_transaction(list_of_transactions, day, type, description):
    """
    The function searches if there exists a transaction with a certain day, type and description
    :param list_of_transactions: the list of transaction
    :param day: the day of the transaction the user is looking for
    :param type: the type of the transaction the user is looking for
    :param description: the description of the transaction the user is looking for
    :return: True if there exists a transaction with such specifications, False otherwise
    """
    for transaction in list_of_transactions:
        if transaction['type']==type and transaction['description']==description and str(transaction['day'])==(day):
            return True
    return False

def find_is_description(list_of_transactions, description):
    """
    The function searches if there exists a transaction with a certain description
    :param list_of_transactions: the list of transactions
    :param description: the type of the transaction the user is looking for
    :return: True if there exists a transaction with such description, False otherwise
    """
    for transaction in list_of_transactions:
        if transaction['description']==description:
            return True
    return False

def build_table(list_of_transactions):
    """
    The function build a table of all the transactions from the list
    :param list_of_transactions: the list of transactions
    :return: a python texttable
    """
    table=Texttable()

    table.add_row(['Day','Value','Type','Description'])
    for i in range(len(list_of_transactions)):
        table.add_row([ get_day(list_of_transactions[i]), get_value(list_of_transactions[i]), get_type(list_of_transactions[i]),get_description(list_of_transactions[i])])
    return table

def build_table_type(list_of_transactions,type):
    """
    The function build a table of all the transactions from the  having a certain type
    :param list_of_transactions: the list of transactions
    :return: a python texttable
    """
    table = Texttable()
    table.add_row([ 'Day', 'Value', 'Type', 'Description'])
    for i in range(len(list_of_transactions)):
        if list_of_transactions[i]['type']=='in':
            table.add_row([get_day(list_of_transactions[i]), get_value(list_of_transactions[i]),
                           get_type(list_of_transactions[i]), get_description(list_of_transactions[i])])
    return table

def build_table_quantifier(list_of_transactions,quantifier, value_to_compare):
    """
    The function build a table of all the transactions from the list whose value have a certain relation to a quantifier
    :param list_of_transactions: the list of transactions
    :return: a python texttable
    """
    table = Texttable()
    table.add_row([ 'Day', 'Value', 'Type', 'Description'])
    for i in range(len(list_of_transactions)):
        if quantifier == ">" and list_of_transactions[i]['value'] > int(value_to_compare):
            table.add_row([ get_day(list_of_transactions[i]), get_value(list_of_transactions[i]),get_type(list_of_transactions[i]), get_description(list_of_transactions[i])])
        elif quantifier == '<' and list_of_transactions[i]['value'] < int(value_to_compare):
            table.add_row([ get_day(list_of_transactions[i]), get_value(list_of_transactions[i]),get_type(list_of_transactions[i]), get_description(list_of_transactions[i])])
        elif quantifier == '=' and list_of_transactions[i]['value'] == int(value_to_compare):
            table.add_row([ get_day(list_of_transactions[i]), get_value(list_of_transactions[i]), get_type(list_of_transactions[i]), get_description(list_of_transactions[i])])
    return table

if __name__ == '__main__':
    f=open("doc.html", "wt")
    f.write(pdoc("functions.py", ""))
    f.close()