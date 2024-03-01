# first_symbol = float(input("1st num:  "))
# operator = input("operator:  ")
# second_symbol = float(input("2nd num:  "))
#
# # result = 0
#
# # if operator not in "+-*/" or len(operator) != 1:
# if operator not in ["+", "-", "*", "/"]:
#     result = "ERROR - something goes wrong"
# elif operator == "+":
#     result = first_symbol + second_symbol
# elif operator == "-":
#     result = first_symbol - second_symbol
# elif operator == "*":
#     result = first_symbol * second_symbol
# elif operator == "/" and second_symbol == 0:
#     result = "ERROR - can't divide by zero"
# elif operator == "/":
#     result = first_symbol / second_symbol
# else:
#     result = "hhhhhh"
#
# print(result)
#
#
# match operator:
#     case "+":
#         result = first_symbol + second_symbol
#     case "/":
#         if second_symbol == 0:
#             result = "ERROR - can't divide by zero"
#         else:
#             result = first_symbol + second_symbol
#     case _:
#         result = "hhhhhh"
#
#
#
# original_list =  [12, 3, 4, 5, 8]
#
# if len(original_list) > 1:
#     original_list.insert(0, original_list.pop())
#
# print(original_list)


# str
# str methods(lower, upper, capitalize, isalpha, rfind, replace, startwith)

# value_str = "hello"
# print(id(value_str))
# value_str = "hello!"
# print(id(value_str))

# print(value_str[::2])
# print(value_str[::-1])
# print(value_str[1:3])
# print(value_str[10])
# print(value_str[10:])

# for letter in value_str:
#     print(letter)
#
# for index in range(len(value_str)):
#     print(index)

# enumerate()

# for index, letter in enumerate(value_str):
#     print(index, letter)


# value_list = [1, 2, 3]
# value_str = str(value_list)
# print(value_str, type(value_str))

# value_str = "Hello World lllll"
# value_str_1 = value_str.lower()
# value_str_2 = value_str.upper()
# value_str_3 = value_str.capitalize()
# value_str_4 = value_str.title()
# value_str_5 = value_str.swapcase()
#
# # print(value_str, id(value_str))
# print(value_str_3, id(value_str_3))
# print(value_str_4, id(value_str_4))
# print(value_str_5, id(value_str_5))
# value = ""
# # value_is_digit = value_float.isdigit()
# # value_is = value_float.isalpha()
# # value_is = value_float.isspace()
# print(value)
#
# for letter in value_float:
#     # if letter.isdigit():
#     #     value += letter
#     if letter.isalpha():
#         value += letter
#
# print(value)


# print(value_float, value_is)

# value = "Hello/World/kkk"

# for letter in value_float[method+1:]:
#     pass


# method = value_float.find("l")
# method_2 = value_float.rfind("l")
# print(method)
# print(method_2)
# method = value_float.index("l")
# print(method)


# # split()
# value = "c/Documents/kkk.png.png.png"
#
# some_method = value.split(".")
# print(some_method)
# some_method[-1] = 'jpeg'
# print(some_method)
#
# # join()
#
# result = ".".join(some_method)
# print(result)

# replace()
# print(value)
#
# result = value.replace(".png", ".jpeg", 1)
# index = result.find(".png")
#
# result_1 = result[:index]
# print(result_1)

# strip()
# rstrip()
# lstrip()
#
# value = "    Nick Welcome Hi"
# print(value)
#
# result = value.strip("_")
# # result = value.rstrip("_")
# # result = value.lstrip("_")
# print(result)


###### ASCII ########

# alphabet = ""
# value = "y"
# print(ord(value))
# value = chr(ord(value)+1)
# print(value)
# print(chr(100))

# for index_of_charecter in range(ord("A"), ord("Z")+1):
#     alphabet += chr(index_of_charecter)
#     # print(chr(index_of_charecter), index_of_charecter)
#
# print(alphabet)

# import this
#
# print(this)

some_list = [1, 23, 4]
# some_list.sort(key=)
