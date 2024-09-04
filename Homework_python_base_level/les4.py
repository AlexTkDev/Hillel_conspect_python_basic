#               ---------------- EX 1 -----------------
#
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# temp_list = [i for i in my_list if i == 0]
# my_list = [i for i in my_list if i != 0] + temp_list
# print(my_list)


# option two
#
# my_list = [1, 0, 13, 0, 0, 0, 5, 9, 9, 9, 9, 0, 0, 0, 0, 6, 7, 5, 4, 3, 6, 7, 5, 4, 3, 0, 6, 7, 5,
#            4, 3, 6, 7, 5, 4, 3]
#
# my_list.sort(key=bool, reverse=True)
# print(my_list)


# options three
#
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# for i in range(len(my_list)):
#     if my_list[i] == 0:
#         my_list.remove(0)
#         my_list.append(0)
#
# print(my_list)


#               ---------------- EX 2 -----------------

# my_list = [0,1,2]
# result = 0
#
# if len(my_list) == 0:
#     result = 0
# else:
#     for i in my_list[::2]:
#         result += i
#     result *= my_list[-1]
#
# print(result)


# option two
#
# my_list = [0, 1, 2]
# result = 0
#
# for i in range(0, len(my_list), 2):
#     result += my_list[i]
#
# if my_list != []:
#     result *= my_list[-1]
#
# print(result)


# options three
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = sum(my_list[::2] * my_list[-1])
# print(result)