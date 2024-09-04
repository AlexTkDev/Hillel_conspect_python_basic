#                       ------------------  EX 1  ---------------------
from inspect import isgenerator


def prime_generator(end):
    # option 1
    # is_prime = (num for num in range(2, end + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    # return is_prime

    # # option 2
    def is_prime(val):
        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok!')


#                       ------------------  EX 2  ---------------------


def is_even(number):
    # print(bin(number))
    # return (number & 1) == 0

    # or
    str_number = str(number)
    if str_number[-1] in ("2", "4", "6", "8", "0"):
        return True
    else:
        return False


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok!')
