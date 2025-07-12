import functions
import copy

# --tests A ---
def test_add_transaction():
    history=[]

    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}]
    functions.add_transaction(history,list_of_transactions,100, 'in', 'gift')
    assert list_of_transactions[1]['day'] == 5
    assert list_of_transactions[1]['value'] == 100
    assert list_of_transactions[1]['type'] == 'in'
    assert list_of_transactions[1]['description'] == 'gift'



def test_insert_transaction():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]
    list_of_transactions=functions.insert_transaction(history,list_of_transactions,16, 10, 'out', 'pizza')
    assert list_of_transactions[1]['day'] == 16
    assert list_of_transactions[1]['value'] == 10
    assert list_of_transactions[1]['type'] == 'out'
    assert list_of_transactions[1]['description'] == 'pizza'


# --tests B ---
def test_remove_day():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]
    list_of_transactions=functions.remove_day(history,list_of_transactions, 5)
    assert list_of_transactions==[{'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]

def test_remove_from_to():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                          {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]
    list_of_transactions=functions.remove_from_to(history,list_of_transactions, 4,5)
    assert list_of_transactions==[{'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]

def test_remove_type():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                          {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]
    functions.remove_type(history,list_of_transactions, 'out')
    assert list_of_transactions==[{'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]

def test_modify_value():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                          {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]
    list_of_transactions=functions.modify_value(history,list_of_transactions, 5, 100, 'out', 'pizza')
    assert list_of_transactions==[{'day': 5, 'value': 100, 'type': 'out', 'description': 'pizza'},{'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}, {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]




















def test_filter_type():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                          {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]
    functions.filter_type(history,list_of_transactions,  'out')
    assert list_of_transactions==[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'},{'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]

def test_filter_type_value():
    history=[]
    list_of_transactions=[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'}, {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                          {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]
    functions.filter_type_value(history,list_of_transactions,  'out', 60)
    assert list_of_transactions==[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'},{'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'}]

def test_calculate_balance():
    list_of_transactions = [{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'},
                            {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'},
                            {'day': 4, 'value': 10, 'type': 'out', 'description': 'groceries'},
                            {'day': 4, 'value': 5, 'type': 'in', 'description': 'cash'}]
    balance=functions.calculate_balance(list_of_transactions, 4)
    assert balance==-5

def test_undo_operation():
    history=[]
    list_of_transactions = [{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'},
                            {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]
    history.append(copy.deepcopy(list_of_transactions))
    functions.insert_transaction(history, list_of_transactions, 4, 100, 'out', 'drinks')
    list_of_transactions=functions.undo_operation(history)
    assert list_of_transactions==[{'day': 5, 'value': 50, 'type': 'out', 'description': 'pizza'},
                            {'day': 23, 'value': 5000, 'type': 'in', 'description': 'salary'}]
test_add_transaction()
test_insert_transaction()
test_remove_day()
test_remove_from_to()
test_remove_type()
test_modify_value()
test_filter_type()
test_filter_type_value()
test_calculate_balance()
test_undo_operation()
