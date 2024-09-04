

import string, keyword

# my_string = '_'  # Вивід: True
# my_string = 'x'  # Вивід: True
# my_string = 'get_value'  # Вивід: True
# my_string = 'get value'  # Вивід: False
# my_string = 'get!value'  # Вивід: False
# my_string = 'some_super_puper_value'  # Вивід: True
# my_string = 'Get_value'  # Вивід: False
# my_string = 'get_Value'  # Вивід: False
# my_string = 'getValue'  # Вивід: False
# my_string = '3m'  # Вивід: False
# my_string = 'm3'  # Вивід: True
#
# result = True
# if my_string[0].isdigit():
#     result = False
# if my_string in keyword.kwlist:
#     result = False

# for letter in my_string:
#     if not result:
#         break
#     if letter.isupper():
#         result = False
#         break
#     if letter == "_":
#         continue
#     if letter in string.punctuation or letter.isspace():
#         result = False
#         break
#
# print(result)


# my_string = input("Please enter your variable: ")
# result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
# print(result)



# value = "      Nick__________        "
#
# value = value.strip().strip("_")
# print(value)



#
#
# Modified calculator

while True:
    number_1 = input('Enter the first number: ')
    if not number_1.isdigit():
        print('Undefined number! Try again.')
        continue
    number_1 = float(number_1)

    action = input('Enter the operator: ')
    if action not in ('+', '-', '/', '*'):
        print('Undefined action! Try again.')
        continue

    number_2 = input('Enter the second number: ')
    if not number_2.isdigit():
        print('Undefined number! Try again.')
        continue
    number_2 = float(number_2)

    result = 0

    if action == '+':
        result = number_1 + number_2
        print(result)
    elif action == '-':
        result = number_1 - number_2
        print(result)
    elif action == '*':
        result = number_1 * number_2
        print(result)
    elif action == '/' and number_2 == 0:
        result = str('Ділення на нуль неможливе!')
        print(result)
    else:
        result = number_1 / number_2
        print(result)

    var_cont = input('Do you want to continue? Y/N? ')
    if var_cont.lower() != 'y':
        print('Good bye!')
        break





# collections OrderedDict (popitem, move_to_end)
#
# from collections import defaultdict
#
# for i in range(5):
#     defdict[i].append(i * 5)
#
# print(defdict)
#
# dict_one = {}
#
# for i in range(5):
#     dict_one.setdefault(i, [])
#     dict_one[i].append(i * 5)
# print(dict_one)
#


# from collections import namedtuple
# fields = ('color', 'engine')
# car = namedtuple('Car', fields)
# car1 = car('red', 2000)
# car1._asdict()
# # color1, engine1 = car1
# # print(color1, engine1)
# print(car1._asdict())



# max(), min(), sum()

from collections import OrderedDict, defaultdict

# value_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
# print(value_dict)
#
# my_order_dict = OrderedDict(value_dict)   # [("name", "Nick"), ("age", 18), ("country", "Ukraine")]
# print(my_order_dict.popitem())


# this_dict = dict.fromkeys(('name', 'age', 'key_3'), [])
#
# print(this_dict)
# this_dict["name"].append(2)
#
# print(this_dict)


my_dict = defaultdict(list)

for i in range(5):
    my_dict[i].append(i * 5)

print(my_dict)


# from collections import namedtuple
#
# fields = ('color', 'engine')
#
# car = namedtuple('Car', fields)
#
# car_1 = car('red', 2000)
#
# # print(car_1)
#
# color_1, engine_1 = car_1
#
# # print(color_1, engine_1)
#
# # print(car_1.color)
# # print(car_1.engine)
# print(car_1._asdict())

# set frozenset, .discard, remove, clear

# test = [{"name": "John", "age": 33}]
#
# print(dict(test[0]))


# my_set = {1, 2, 3, "hello", "red"}
# my_list = [2, 3, "hello", "red", 1,]
#
# print(1 in my_set)
# print(1 in my_list)
#
# # (1, 2, 3): "rgb"
#
#
# new_val = frozenset(my_set)
# print(new_val)
# number_3 = 10

#
# def math_add(num_1, num_2):
#     result = num_1 + num_2
#     return result
#
#
# def calc(num_1, num_2, operator):
#     if operator == "+":
#         result = math_add(num_1, num_2)
#     return result
#
#
# def get_some_data():
#     """some func"""
#
#
# def send_email():
#     """some func"""
#
#
# print(send_email(2, 3, "+"))
#


# def say_hi(name, age):
#     pass
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')



