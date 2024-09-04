#                       ------------------  EX 1  ---------------------

def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    for i in range(0, end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')


#                       ------------------  EX 2  ---------------------

def is_even(digit):
    """ Перевірка чи є парним число """
    return digit % 2 == 0

    # or
    # return True if digit % 2 == 0 else False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')