# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# list
# змінні не змінні типи даних різниця
# методи list(append(), pop(), sort(), copy())
# функція sorted()

# int
# float
# complex
# decimal

# str

# bool
# None

# list
# dict
# set
# tuple

######### NoneType #######

# value = None
# value = 111
# val_1 = print(value)
# print(val_1)

########### Bool ########


# value_int = 100
# value_float = -0.01
# value_str = ""
# print(bool(value_int) * 2)
#
# value_bool = True
# print(value_bool * 2)


############### Logic Operators ########################### >, <, >=, <=, ==, !=, in, not, is

# value_1 = 10
# value_2 = 5
#
# print(value_1 > value_2)

# print("he" in "hello")
# value_1 = "hello"
# value_2 = "hello"
# print("hello" == "hello")
# print(value_1 is value_2)

# if певна умова:
#     виконуємо цю операцію

# value_int = 11
#
# # and or
#
# # if value_int > 0 and value_int < 10:
# if 0 < value_int < 10:
#     print(f"{value_int} is bigger then 0")
# elif value_int > 10:# else if
#     print(f"{value_int} is bigger then 10")
# else:
#     print(f"{value_int} is not bigger then 0")
#
#
# print("end")


# value_1 = 2000
# value_2 = 330
#
# # if value_1 > value_2:
# #     result = "A"
# # else:
# #     result = "B"
#
# result = "A" if value_1 > value_2 else "B"
#
# print(result)


########### List ###############

# value_list = [1, 2.1, "hello", [1, 2, 3]]    # 0,1,2,3

# print(value_list)
# print(value_list[-1])
# print(value_list[0:2])  # 0 - хводить в діапазон 2 - до(не входить в діапазон)
# print(value_list[1:])  #нема помилки навіть якщо не існує індекса
# print(value_list[-2:10])  #
# print(len(value_list)) # length довжина ліста



# ############################################
#
# base_list = [1, 2, 3]
# my_new_list = base_list * 4
#
# # print(my_new_list)
#
# base_list[0] = 10
#
# print(f"base_list {base_list}")
# print(f"my_new_list {my_new_list}")
#
# # # ######################################
#
# from copy import deepcopy
# # list_2 = [True, False]
# base_list = [1, 2, 3, [True, False]]
#
# new_list = [deepcopy(base_list)] * 4
# # new_list = [link, link, link, link]
# # print(new_list)
# print(new_list)
#
# base_list[-1][0] = 1
# print(f"base_list {base_list}")
# print(new_list)

# # # ######################################
