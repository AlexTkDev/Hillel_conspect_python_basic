#                                  ----------- EX 1 ------------

####################### Calculator using if ######################

# num_1 =int(input('Enter a number 1: '))
# num_2 =int(input('Enter a number 2: '))
# action =input('Enter action: ')
#
# if action == '/':
#     if num_2 != 0:
#         result = num_1 / num_2
#     else:
#         result = 0
# elif action == '+':
#     result = num_1 + num_2
# elif action == '-':
#     result = num_1 - num_2
# else:
#     result = num_1 * num_2
#
# print(f"The result of = {result}")


############## Using the method match ###############
#
# num_1 = int(input('Enter a number 1: '))
# num_2 = int(input('Enter a number 2: '))
# action = input('Enter action: ')
#
# if action == '+' or action == '-' or action == '+' or action == '/' or action == '*':
#     match action:
#         case '/':
#             if num_2 != 0:
#                 result = num_1 / num_2
#             else:
#                 result = 0
#         case '+':
#             result = num_1 + num_2
#         case '-':
#             result = num_1 - num_2
#         case '*':
#             result = num_1 * num_2
# else:
#     result = 'Invalid value, enter +, -, *, / '
#
# print(f'The result is = {result}')

#                                  ----------- EX 2 ------------

# my_list = []
#
# if len(my_list) == 0:
#     result = []
# elif len(my_list) == 1:
#     result = my_list
# else:
#     new_list = my_list.pop(-1)
#     my_list[0] = new_list
#     result = my_list
# print(result)

#################### next method

original_list = [1, 2, 3, 4, 5]

if len(original_list) >1:
    original_list.insert(0, original_list.pop())

print(original_list)
