# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій


# persons = [{"name": "John", "age": 15},
#            {"name": "Anna", "age": 23},
#            {"name": "Dan", "age": 5},
#            {"name": "Maximus", "age": 24},
#            {"name": "Olha", "age": 25},
#            {"name": "Volodymyr", "age": 5},
#            {"name": "Jack", "age": 45}]
#
#
# def exercise_6_1(persons_dict):
#     ages = []
#     names_lens = []
#
#     youngest_persons = []
#     long_name_persons = []
#
#     for person_dict in persons_dict:
#         ages.append(person_dict["age"])                             #put all age
#         names_lens.append(len(person_dict["name"]))                 #put all names
#
#     min_age = min(ages)
#     max_len_name = max(names_lens)
#
#     for person_dict in persons_dict:
#         if person_dict["age"] == min_age:
#             youngest_persons.append(person_dict["name"])
#         if len(person_dict["name"]) == max_len_name:
#             long_name_persons.append(person_dict["name"])
#
#     average_age = sum(ages) / len(ages)
#
#     return [youngest_persons, long_name_persons, int(average_age)]
#
#
# young_persons, longname_person, avrg_age = exercise_6_1(persons)
# print(f"Min ege is: {young_persons,} {longname_person}, {avrg_age}")




# my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
# my_dict_2 = {11: 11, 2: 22}
#
# def exercise_6_2(dict_1, dict_2):
#
#     result_1 = list(set(dict_1.keys()).intersection(set(dict_2.keys())))
#
#     result_2 = list(set(dict_1.keys()).difference(set(dict_2.keys())))
#
#     # result_3 = {}                                        # розгорнутий варіант від дікт компрехеншн
#     #
#     # for key in result_2:
#     #     result_3.update({key: dict_1[key]})
#     #     # result_3[key] = dict_1[key]
#
#     result_3 = {key: dict_1[key] for key in result_2}     # дікт компрехеншн
#
#     result_4 = dict_1.copy()
#     for key in dict_2:
#         if key in result_4:
#             result_4[key] = [result_4[key], dict_2[key]]
#         else:
#             result_4[key] = dict_2[key]
#
#     return result_1, result_2, result_3, result_4
#
#
# print(exercise_6_2(my_dict_1, my_dict_2))


# def add(num_1, num_2):
#     return num_1 + num_2
#
#
# def calc(num_1, num_2):
#     res = 0
#     if num_2 == 0:
#         res = "Error"
#     else:
#         res = add(num_1, num_2)
#
#     return res
#
#
# print(calc(2, 3))


# def my_add(my_list):     # приклад локальних змінних змінний тип данних
#     # my_list = my_list.copy()
#     my_list[0] = my_list[0] + 3
#     summa = 0
#     for elem in my_list:
#         summa = summa + elem
#     return summa
#
# # result = 10
# result_list = [5, 10]
#
# print(my_add(result_list))
# print(result_list)

# LEGB правила доступу до змінних





# from math import pi
#
# pi = 'global'
#
# def outer():
#     pi = 'Enclosing'
#
#     def inner():
#         # pi = 'Local'
#         pi = pi + "!!!"
#         print(pi)
#
#     inner()
#
# outer()
# print(pi)


# pi += 1
# pi = 10
#
# print(pi)


# from math import pi
#
#
# def inner():
#     global pi
#     pi += 10
#     # pi = pi + "!!!"
#     # print(pi)
#
#     return "Hello"
#
#
# pi = 5
#
# inner()
#
# for i in range(pi):
#     print(i)

# import operator
#
# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
#
# num_1 = float(input("num_1 "))
# action = input("action ")
# num_2 = float(input("num_2 "))
#
# func = actions.get(action)
# if not func:
#     print("Error")
# else:
#     print(func(num_1, num_2))  # operator.mul(num_1, num_2)


# is_send_second_email = True

# def print_line(w, fill, is_email=False):
#     for i in range(w):
#         print(fill, end="")
#
#     if is_email:
#         print("yes")
#
#     return

# print_line(fill="*", w=6, is_email=is_send_second_email)     # іменований виклик
# print_line(6, "*")


# *args

# my_tuple = (1, 2, 3, 8, 9, 0)
# val_1, *tmp = my_tuple
# print(val_1)
# print(tmp)

# def group(*args):
#     res = {"teacher": "Nick", "students_list": list(args)}
#     # for student in args:
#     #     res["students_list"].append(student)
#     return res
#
# print(group("Nick", "Volodymyr", "Nadiia"))

# def get_min_val(*args):
#     print("!!!!!!!!")
#     # min_val = args[0]
#
#     min_val = None
#     if not args:
#         return "Error"
#     else:
#         min_val = args[0]
#         for i in args:
#             if i < min_val:
#                 min_val = i
#     return min_val
#
# print(get_min_val(1, 2, 3 ))

# max()
# print(min())



# **kwargs   dict() {}

# def say_hello(name):
#     return f"Hello {name}"
# def print_age(age):
#     return f"{age}"
#
# def print_line(w, fill, **kwargs):
#     print(kwargs)
#     if "name" in kwargs:
#         print(say_hello(kwargs.pop("name")))
#     else:
#         print(say_hello("John"))
#
#     print(print_age(kwargs.get("age", 18)))
#
#     for i in range(w):
#         print(fill, end="")
#     return
#
# print_line(w=6, fill="*", name_2="Nick", age=12)






