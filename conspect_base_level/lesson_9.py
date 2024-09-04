
# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#     # return "Hi. My name is Alex and I'm 32 years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'say_hi error: '
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('OK')



# def correct_sentence(text):
#     if text[0].islower():
#         text = text[0].upper() + text[1:]
#     # if text[-1] != '.':
#     if text.endswith('.'):
#         text += "."
#
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'correct_sentence error: forgot about capital letter and dot'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('OK')


# def draw_rectangle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end="")
#
#     return None
#
# # draw_rectangle(7, 5, "*")
#
#
# # my_args = 7, 5, "*"
# # draw_rectangle(*my_args)
#
# # my_args = [7, 5, "*"]
# my_value = (7, 5, "*")
# draw_rectangle(*my_value)

# args     (1, 2, 3)   *
# kwargs   {"name": 8} **


# def my_add(num_1, num_2):
#     return num_1 + num_2
#
# # print(my_add(2, 3))
# print(my_add)
#
# my_math_adding = my_add
# print(my_math_adding(9, 8))


# def my_add(num_1, num_2):
#     return num_1 + num_2
#
#
# def my_mul(num_1, num_2):
#     return num_1 * num_2
#
#
# func_list = [my_add, my_mul]
# print(func_list)
#
# for func in func_list:
#     print(func(2, 3))


# def my_mul(num_1):
#     return num_1 * 2
#
# def my_add(num_1):
#     return num_1 + 2
#
#
# def map_func(num_list, func):
#     for num in num_list:
#         print(func(num))

# map_func([1, 2, 3], my_mul)
# map_func([1, 2, 3], my_add)

# choice = 0
#
# if choice == 1:
#     def my_func(n):
#         if n > 0:
#             return 1
#         else:
#             return 0
# else:
#     def my_func(n):
#         if n < 0:
#             return 1
#         else:
#             return 0
#
# print(my_func(10))

# def my_func(n):
#     if n > 0:
#         return 1
#     else:
#         return 0
#
# def my_func():
#     return 10
#
# print(my_func())

# print(my_func.__name__)
# print(my_func.__module__)

# if __name__ == "__main__":
#     print("!!!!!!!!!")


# from lesson_8 import my_func
#
# # print(my_func.__module__)
#
# print(my_func())


# def my_func():
#     return 10
#
#
#
# if __name__ == "__main__":
#     print(my_func.__module__)
#     print("!!!!!!!!!")





# def my_func(n):
#     """This func is doing something. IMPORTANT: """
#
#     if n > 0:
#         return 1
#     else:
#         return 0
#
#
#
#
#
# my_func()

# def my_func():
#     """This func is doing something. IMPORTANT: """
#
#
# # print(str.__doc__)
# print(my_func.__doc__)

#
# def my_add(num_1: int, num_2: int) -> int:
#     return num_1 + num_2
#
# print(my_add("2", "2"), type(my_add("2", "2")))



#  Рекурсія

# def fibo(n):
#
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#
# print(fibo(10))

# def fibo(n):
#
#     # print(n)
#
#     if n in (1, 2):
#         return 1
#     return fibo(n-1) + fibo(n - 2)
#
# print(fibo(10))


# lambda()



# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# sequence = [0, 9, 8 -4, 2]

# def bigger_than_zero(x):
#     return x > 0
#
# bigger_than_zero = lambda x: x > 0

# res = my_filter(sequence, lambda x: x > 0)
# res = my_filter(sequence, lambda x: not x % 2 == 0)
# res = my_filter(sequence, bigger_than_zero)

# print(res)


# map() filter() zip()

# map works with str, list, tuple

# valu_str = "1234"
#
# int_nums = []
# for i in valu_str:
#     int_nums.append(int(i))

# int_nums = map(int, "1234")
#
# print(int_nums)
# print(list(int_nums))

# def power(x):
#     return x ** 2

# numbers = [1, 2, 3, 4]
#
# # power_numbers = map(power, numbers)
# power_numbers = map(lambda x: x**2, numbers)
#
# print(numbers)
# print(list(power_numbers))


# filter()

# numbers = [1, -4, 0, 2, 3, 4]
# numbers = "120345"
# # filter_nums = filter(None, numbers)
# filter_nums = filter(lambda x: int(x) > 0, numbers)
#
# print(list(filter_nums))


# zip()

# numbers_3 = [1, -4, 0, 2, 3, 4]
# numbers_2 = ("apple", "red", "true")
# numbers_1 = "uiuiiiuiu"
#
# for element in zip(numbers_1, numbers_2, numbers_3):
#     print(element)












