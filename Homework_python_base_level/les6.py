# #                   ------------------- EX 1 --------------------
#
# users = [{"name": "John", "age": 15},
#          {"name": "Jack", "age": 45},
#          {"name": "Alex", "age": 35},
#          {"name": "Nicolas", "age": 15},
#          {"name": "Ann", "age": 25},
#          {"name": "Tod", "age": 24},
#          {"name": "Tonni", "age": 18},
#          ]
#
# min_age = min(age["age"] for age in users)
# jr_names = [name["name"] for name in users if name["age"] == min_age]
#
# max_long_name = max(len(name["name"]) for name in users)
# longest_name = [name["name"] for name in users if len(name["name"]) == max_long_name]
#
# md_age = sum(age["age"] for age in users) / len(users)
# middle_age = round(md_age, 2)
#
# print(f"а) Ім'я наймолодшої людини: {jr_names}\n"
#       f"б) Найдовше ім'я: {longest_name}\n"
#       f"в) Середній вік усіх людей = {middle_age}"
#       )


#                   ------------------- EX 2 --------------------
#
# my_dict_1 = {1: 1, 22: 2, 3: 3, 4: 4, 5: 5, 67: 6}
# my_dict_2 = {1: 1, 9: 2, 3: 10, 4: 4, 5: 8, 6: 7}
#
# in_two_dict = [key for key in my_dict_1.keys() if key in my_dict_2]
#
# only_first_keys = [key for key in my_dict_1.keys() if key not in my_dict_2]
#
# only_in_the_first = {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}
#
# merged_dict = {}
# for key, value_1 in my_dict_1.items():
#     if key in my_dict_2:
#         merged_dict[key] = [value_1, my_dict_2[key]]
#     else:
#         merged_dict[key] = value_1
#
# for key, value_2 in my_dict_2.items():
#     if key not in my_dict_1:
#         merged_dict[key] = value_2
#
# print(f"a) Список із ключів, які є в обох словниках: {in_two_dict}\n"
#       f"б) Список із ключів, які є у першому, але немає у другому словнику: {only_first_keys}\n"
#       f"в) Значення для ключів, які є в першому, але немає в другому словнику: {only_in_the_first}\n"
#       f"г) Об'єднання двох словників: {merged_dict}"
#       )


# option two
# my_dict_1 = {1: 1, 22: 2, 3: 3, 4: 4, 5: 5, 67: 6}
# my_dict_2 = {1: 1, 9: 2, 3: 10, 4: 4, 5: 8, 6: 7}
#
# # a
# in_two_dict = set(my_dict_1.keys()) & set(my_dict_2.keys())
# list_in_two_dict = list(in_two_dict)
# print(list_in_two_dict)
#
# # b
# only_first_keys = set(my_dict_1.keys()) - set(my_dict_2.keys())
# list_in_only_first_keys = list(only_first_keys)
# print(list_in_only_first_keys)
#
# # c
# only_in_the_first = set(my_dict_1).difference(my_dict_2)
# new_keys = {}
# for key, value in my_dict_1.items():
#     if key in only_first_keys:
#         new_keys[key] = value
# print(new_keys)
#
# # d
# merged_dict = {}
# new_set = set(my_dict_1).union(set(my_dict_2))
#
# for key in new_set:
#     if key in my_dict_1 and key in my_dict_2:
#         merged_dict[key] = [my_dict_1[key], my_dict_2[key]]
#     elif key not in my_dict_2:
#         merged_dict[key] = my_dict_1[key]
#     else:
#         merged_dict[key] = my_dict_2[key]
#
# print(merged_dict)

# option three
dict_1 = {1: 1, 22: 2, 3: 3, 4: 4, 5: 5, 67: 6}
dict_2 = {1: 1, 9: 2, 3: 10, 4: 4, 5: 8, 6: 7}


def work_to_dictionary(my_dict_1, my_dict_2):
    result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2)))

    result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2)))

    result_3 = {key: my_dict_1[key] for key in result_2}

    result_4 = my_dict_1.copy()
    for key in my_dict_2:
        if key in result_4:
            result_4[key] = [result_4[key], my_dict_2[key]]
        else:
            result_4[key] = my_dict_2[key]

    return (f'a) Список із ключів, які є в обох словниках: {result_1}\nб) Список із ключів, які є у першому,'
            f' але немає у другому словнику: {result_2}\nв) Значення для ключів, які є в першому,'
            f' але немає в другому словнику: {result_3}\nг) Об\'єднання двох словників: {result_4}')


print(work_to_dictionary(dict_1, dict_2))
