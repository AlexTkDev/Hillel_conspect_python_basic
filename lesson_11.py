
# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', 'was', 'three', 'near']
#
#
# def popular_words(txt, wrds):
#     text_words = txt.lower().split()
#     popular_dict_words = {}
#
#     for word in wrds:
#         popular_dict_words.update({word: text_words.count(word)})
#
#     # popular_dict_words = {word: text.lower().split().count(word) for word in words}
#     # popular_dict_words = {word: text_words.count(word) for word in words}
#     # popular_dict_words = {word: words.count(text_words) for word in words}
#     # popular_dict_words = {word: 0 for word in words}
#     #
#     # for word in text_words:
#     #     if word in words:
#     #         popular_dict_words[word] += 1
#     return popular_dict_words
#     # return {word: text.lower().split().count(word) for word in words}
#
#
# print(popular_words(text, words))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# def difference(*args) -> Union[int, float]:
#     if args:
#         result = round(max(args) - min(args), 2)
#         return result
#
#     return 0
#
# def difference(*numb_args):
#     if not numb_args:
#         # result = 0
#         return 0
#     # else:
#
#     result = max(numb_args) - min(numb_args)
#     return round(result, 2)
#
# print(difference(5, -5))
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

# write
# writelines

# filename = "test.txt"

# my_file = open(filename, "w")   # "r", "w", "a"

# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
#
# my_file.close()


# val_list = ["Hello World!", "Apple", "Red", "green"]
# my_file = open(filename, "w")
# for i in val_list:
#
#     my_file.writelines(i + "\n")
#
# my_file.close()

# filename = "test.txt"
#
# with open(filename, "w") as my_file:
#     my_file.write("Hello World!\n")
#     my_file.write("Hello World!\n")
#     my_file.write("Hello World!\n")

# filename = "test.txt"
#
# with open(filename, "w") as my_file:
#     for i in val_list:
#         my_file.writelines(i + "\n")

filename = "test.txt"
# filename = "C:/doc/desktop/test.txt"

# my_file = open(filename, "r")
# data = my_file.read()
# print(data, type(data))
# my_file.close()

# with open(filename, "r") as my_file:
#     data = my_file.read()
#
#
# print(data, type(data))


# with open(filename, "r") as my_file:
#     data = my_file.readlines()
#
# print(data)

# with open(filename, "r") as my_file:
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())

# with open(filename, "a") as my_file:
#     data = my_file.write("\nHello")

# with open(filename, "a+") as my_file:
#     data = my_file.write("\nHell9999o")
#     # print(data)
#     my_file.seek(4)
#     context = my_file.read()
#
# print(context)

# with open(filename, "rb") as my_file:    # t - text(default), b - binary ex image
#     data = my_file.write("\nHell9999o")
#
# print(data)


# with open(filename, "r", encoding="UTF-8") as my_file:    # t - text(default), b - binary ex image
#     data = my_file.write("\nHell9999o")
#
# print(data)

class MyCar:
    color = "red"             # атрибут класу
    engine = 2000



# class MyCar(object):
#     color = "red"
#     engine = 2000

car_1 = MyCar()                 # екземпляр класу
car_1.color = "green"            # атрибут екземпляру класу
car_1.body = "sedan"
# print(car_1.color)
# print(car_1.engine)
# print(car_1.body)
#
# car_2 = MyCar()
# print(car_2.color)
# print(car_2.engine)
# # print(car_2.body)

val_str = "hello"
val_str.join()
print(type(val_str))
str
























