""" Solvo: Java test in python """
""" Python Version: 3.5.3 """

__author__ = "Guillermo Esteban Castro Sánchez"
__email__ = "guillermoestebancs@gmail.com"


list = [29, 18, 6, 25, 5, 15, 19, 3, 45, 2]


def get_number_divisors(number):
    ''' Get the numbers who are divisor of other number in the list.'''
    number_divisors = []
    for number_in_list in list:
        if number % number_in_list == 0:
            number_divisors.append(number_in_list)
    return number_divisors


def get_number_dividens(number):
    ''' Count how many dividends has a divisor.'''
    number_dividends = []
    for number_in_list in list:
        if number_in_list % number == 0:
            number_dividends.append(number_in_list)
    return number_dividends


def sort_list():
    '''Sort the list putting first even and then odd numbers.'''
    for number_in_list in list:
        if number_in_list % 2 == 0:
            list.remove(number_in_list)
            list.insert(0, number_in_list)


print('1. Numbers who are divisor of other number in the list: ')
for value, number_in_list in enumerate(list):
    print('Divisors of {} = {}'.format(
        list[value], get_number_divisors(list[value])))
print('2. How many dividends has a number in the list: ')
for value, number_in_list in enumerate(list):
    print('Dividends of {} = {}'.format(
        list[value], len(get_number_dividens(list[value]))))
print('3. List sorted putting first even and then odd numbers: ')
sort_list()
print(list)
