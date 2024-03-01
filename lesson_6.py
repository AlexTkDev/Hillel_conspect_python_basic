# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


# # 1
# value_list = [1, 0, 3, 0]
# for zero in range(len(value_list) - 1, -1, -1):
#     if value_list[zero] == 0:
#         value_list.append(value_list.pop(zero))
#
# print(value_list)
#
# # 2
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# second_list = []
# zero = my_list.count(0)
# for index in range(len(my_list)):
#     if my_list[index] != 0:
#         second_list.append(my_list[index])
# second_list.extend([0] * zero)
# print(second_list)
#
# # 3
# my_list = [1, 0, 13, 0, 0, 0, 5, 9, 9, 9, 9, 0, 0, 4, 3]
#
# my_list.sort(key=bool, reverse=True)
# print(my_list)
#
# # 4
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# for i in range(len(my_list)):
#     if my_list[i] == 0:
#         my_list.remove(0)
#         my_list.append(0)
#
# print(my_list)
#
#
# # 5
# my_list = [0, 3, 5, 0, 4, 0, 7, 9]
# index = 0
# for i in range(len(list)):
#     if list[i] != 0:
#         list[i], list[index] = list[index], list[i]
#         index += 1
# print(list)


# my_list = [0, 1, 7, 2, 4, 8]
# result = 0
#
# for i in range(0,len(my_list),2):
#     result += my_list[i]
#
# if my_list != []:
#     result = result * my_list[-1]
#
# print(result)


# some_list = [0, 4, 5, 2, 6, 7, 4, 2, 1, 7]
# result = sum(some_list[::2]) * some_list[-1]
# print(result)


# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


# my_list = [
#     0,
#     1,
#     7,
#     2,
#     9,
#     10,
# ]
# some_list = []
# for i in range(5):
#     some_list.append(i)
# print(some_list)


# some_list = [i**2 for i in range(5)]
# print(some_list)

# some_list = []
# for i in range(5):
#     if i % 2:
#         some_list.append(i**2)
# print(some_list)

# some_list = [i**2 for i in range(5) if i % 2]
# print(some_list)


# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())

#  tuple
# value_list = [1, 23, 4]
#
# value_tuple = (1, 23, 4)

# value_tuple = tuple()
# value_tuple = (1,)
#
# print(value_tuple, type(value_tuple))

# value_tuple = (1, 4, True, [1, 2, 3])
# print(value_tuple, type(value_tuple), id(value_tuple))
# #
# # value_tuple[-1].append("apple")
# #
# # print(value_tuple, type(value_tuple))
#
# # value_tuple[0]
# # value_tuple[0:]
# # value_tuple[::2]
#
# value_list = list(value_tuple)
#
# print(value_list, type(value_list))
#
# value_tuple = tuple(value_list)
#
# print(value_tuple, type(value_tuple), id(value_tuple))
#
# value_tuple = (1, 4)
# length, _ = value_tuple
#
# print(length)
# print(_)
#
# for _ in range(5):
#     print("Hello")

# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())

############ dict ############ key: value

# value_dict = dict()
# value_dict = {}

# value_dict = dict(John=26, Andrew=28)
# print(value_dict)

# value_dict = {
#     "John": 26,
#     1: 28,
#     1.5: 28,
#     True: 28,
#     None: 28,
#     (1, 2, 3): 28,
# }

# print(hash("John"))
# print(hash(1))
# print(hash(1.5))
# print(hash(True))
# print(hash([1, 2]))

# MD5 SHA256


# print(value_dict)

# value_dict = {
#     "John": 26,
#     1: 28,
#     1.5: True,
#     True: [1,23,3],
#     None: 28,
#     (1, 2, 3): [
#         {
#             "name": "John",
#             "age": 28,
#             "city": "New York",
#             "grade": 1,
#         },
#         {
#             "name": "Nick",
#             "age": 20,
#             "city": "New York",
#             "grade": 3,
#         }
#     ],
# }
#
# print(value_dict[None])
#
# value_dict[None] = 12
#
# print(value_dict[None])
#
# value_dict["None"] = 12
#
# print(value_dict)
#
# person_1 = {
#             "name": "Nick",
#             "age": 20,
#             "city": "New York",
#             "grade": 3,
#         }
#
# person_2 = {
#             "name": "John",
#             "age": 27,
#             "city": "New York",
#             "grade": 1,
#         }
#
# group = [person_1, person_2]
#
# for i in person_1:
#     print(i, person_1[i])

# for key, value in person_1.items():
#     print(key, value)

# for key in person_1.keys():
#     print(key)

# for value in person_1.values():
#     print(value)

# this_dict = dict.fromkeys(('name', 'age', 'key_3'))
# this_dict["name"] = "Nick"
# print(this_dict)
# request = {}
# name = person_1.get("name", None)

# email = request.get("email", False)
# if not email:
#     print("error")
#
# print(name)


# print(person_1)
# name = person_1.pop("name")
# print(name)
# print(person_1)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# print(car)
# car["color"] = "White"
# car.update({"color": "White"})
#
# print(car)


# some_list = [i**2 for i in range(5)]
# print(some_list)

# dict comprehension

# value_dict = {i: f"This is {i}" for i in range(1, 7)}
# print(value_dict)
#
# value_dict = {
#   1: 'This is 1',
#   2: 'This is 2',
#   3: 'This is 3',
#   4: 'This is 4',
#   5: 'This is 5',
#   6: 'This is 6'
# }

####### SET #########

# value_set = set()
# value_list = [1, "apple", 3, "bug", 5, 1, 1, 1]
# # value_tuple = (1, "apple", 3, "bug", 5, 1, 1, 1)
# # value_str = "apple"
#
# value_set = set(value_list)
# new_value_list = list(value_set)
# # print(value_list)
# # print(value_set)
# # print(new_value_list)
#
# value_set_1 = {1, 2, 3}
# value_set_2 = {7, 6, 5, 1, 2}
#
# # print(value_set_1.union(value_set_2))   # + обʼєднання
# #
# # # difference()
# # print(value_set_1.difference(value_set_2)) # - різниця
#
# # intersection()
# # print(value_set_1.intersection(value_set_2)) # перехресний

value_str = "kljkljkljlk"

result = True

if value_str.isupper:
    result = False


print(result)
if result:
    print("it's valid variable")
else:
    print("it's invalid variable")



