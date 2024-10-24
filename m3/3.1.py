# Пространство имён
from tabnanny import check

calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string, search):
    string = string.upper()
    for i in search:
        if i.upper() in string:
            count_calls()
            return True
    count_calls()
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)