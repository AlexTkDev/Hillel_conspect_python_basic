# match/case
# list
# while
# break і continue
# while - else
# for
# for - else
# range()

# comment - ctrl + / (Win), command + /

# input = int(input("Please type some num(4 digit): "))
#
# thousands = input // 1000
# hundreds = input // 100 % 10
# tens = input // 10 % 10
# ones = input % 10
#
# print(f"{thousands}\n{hundreds}\n{tens}\n{ones}")

# a, b, *left_1 = (1)
# print(a)
# print(b)
# print(left_1)


# my_input = int(input("please add 4 digits: "))
# thousands, left_1 = divmod(input, 1000)
# hundreds, left_2 = divmod(left_1, 100)
# tens, ones = divmod(left_2, 10)
#
# # Results printing
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)

# action = ""
#
# if (action == "+") or (action == "-"):
#     print("!!!!!!!!!")
# else:
#     print("&&&&&&&&&&")

# weather = [1, 2]
#
# match weather:
#     case "cold":
#         print("It's cold")
#     case "hot":
#         print("It's hot")
#     case "raining":
#         print("It's raining")
#     case _:
#         print("Not weather")

############ list #############

# value_list = [1, 3, 9]   #88 bytes
# # value_list = ["apple", "red", "true", "aapple"]
#
# value_list.append("Hello")
#
# print(value_list)
#
# some_value = value_list.pop()
#
# print(some_value)
# print(value_list)
#
#
# value_list.reverse()
# print(value_list)
# # value_list.sort(reverse=False, key=len)
# # value_list_1 = sorted(value_list, reverse=True)
# # print(value_list_1)
#
# value_list.insert(5, "oooo")
# # print(value_list)
# # print(len(value_list))
# print(value_list)
#
#
# value_list = [1, 3, 9]   #88 bytes
# value_list.append(2)  #88 bytes

############ Loop ############

# while  for
value_int = 0
is_true = True

# while True:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         break
# else:
#     print("dddddd")

# while value_int < 10:
#     value_int += 1
#     print(value_int)
#
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         is_true = False
# else:
#     print("dddddd")
#
# print("end")

# continue
# while is_true:
#     value_int += 1
#
#     if value_int == 5:
#         continue
#
#     print(value_int)
#     if value_int > 10:
#         is_true = False
# else:
#     print("dddddd")
#
# print("end")


# # for, for - else, range()

# some_str = "hello"

# [1,2,3,4]
# (1,2,3,4)
# "hello"
# index = 0
# for letter in some_str:
#     print(letter)


# while index < len(some_str):
#     print(some_str[index])
#     index += 1


# range(5)  - (0-4)
# range(2, 5)  - (2-4)
# range(2, 5, 2)  - (2-4)

# list_1 = [1, 2, 3, 4, 5]
# print(list_1[::-1])

# for i in range(2, 5, 2):
#     print(i)
#     if i == 4:
#         break
# else:
#     print(11111)
#
#
# print("end")


# for number in range(5):
#     for num_2 in range(5):
#         print(number)
#         if num_2 == 4:
#             break
#     print(number)
# else:
#     print(11111)
#
#
# print("end")

# some_num = input("number: ")
#
# for letter in some_num:
#     print(letter)


# num = input("Data: ")
# index = 0
#
# while index < len(num):
#     print(num[index])
#     index += 1

# while index < len(num):
#    print(num[index])
#    index += 1


# while index < len(num):
#     print(num[index])
#     index += 1

# some_number = input("Numbers: ")
# index = 0
#
# while index < len(some_number):
#     print(some_number[index])
#     index += 1



# some_number = input('Add number: ')
#
# length = len(some_number)
# index = 0
#
# while index < length:
#     print(some_number[index])
#     index += 1