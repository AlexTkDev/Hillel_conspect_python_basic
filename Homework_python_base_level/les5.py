#                           ------------- EX 1 ----------
# modified Calculator

# while True:
#     num_1 = input('Enter a number 1: ')
#     num_2 = input('Enter a number 2: ')
#     action = input('Enter action, or break to exit the program: ')
#     result = None
#
#     if action == 'break':
#         break
#
#     try:
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#     except:
#         result = 'Invalid input entered'
#     else:
#         if action in ('+', '-', '/', '*'):
#             match action:
#                 case '/':
#                     if num_2 != 0:
#                         result = num_1 / num_2
#                     else:
#                         result = 0
#                 case '+':
#                     result = num_1 + num_2
#                 case '-':
#                     result = num_1 - num_2
#                 case '*':
#                     result = num_1 * num_2
#         else:
#             result = 'Invalid value, enter +, -, *, / '
#
#     print(f'The result is = {result}')


#                           ------------- EX 2 ----------
# option 1
#
# from keyword import kwlist
#
# value_name = "_"
# value_name = "x"
# value_name = "get_value"
# value_name = "get value"
# value_name = "get!value"
# value_name = "some_super_puper_value"
# value_name = "Get_value"
# value_name = "get_Value"
# value_name = "getValue"
# value_name = "3m"
# value_name = "m3"
#
# result = True
#
# literal = '''!"#$%&'()*+,-./:;<=>?@[]{}\\^`|~'''
# kw_list = kwlist
#
# if not value_name[0].isdigit() and not value_name[0].isupper():
#     if not value_name.isdigit() and not value_name.isupper():
#         if value_name.find(" ") == -1:
#             if value_name not in kw_list:
#                 for letter in value_name:
#                     if letter not in literal and not letter.isupper():
#                         result = True
#
#                     else:
#                         result = False
#                         break
#         else:
#             result = False
# else:
#     result = False
#
# print(result)

# option 2
#
# import keyword, string
#
# value_name = "_"
# value_name = "x"
# value_name = "get_value"
# value_name = "get value"
# value_name = "get!value"
# value_name = "some_super_puper_value"
# value_name = "Get_value"
# value_name = "get_Value"
# value_name = "getValue"
# value_name = "3m"
# value_name = "m3"
#
#
# value_name = input("Enter value ")
# result = True
#
# if value_name[0].isdigit():
#     result = False
# if value_name in keyword.kwlist:
#     result = False
#
# for letter in value_name:
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

# option 3 - The best
#
# value_name = input("Enter value ")
# result = False
# if value_name.identifier():
#     if value_name == "_" or value_name.islower():
#         result = True
#
# print(result)

