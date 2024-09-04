# def pow(x):
#     return x ** 2

# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     for _ in range(end):
#         yield begin
#         begin = func(begin)
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
#
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')


# def is_even(digit):
#     return digit % 2 == 0
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')


# 3 принципи ООП: Інкапсуляція, Поліморфізм, Наслідування. Якщо загалом то ще додають Абстракцію та Композицію


# class MyCar:
#     # color = "color1111"
#     def __init__(self, color, engine, price, body="sedan"):
#         self.color = color
#         self.engine = engine
#         self.price = price
#         self.body = body
#
#
#
#
#
# car_1 = MyCar("green", 2.0, 20000, 'hatchback')
#
# car_2 = MyCar("gree22222n", 3.0, 20000)
#
# print(car_1)
# print(car_1.color)
# print(car_1.body)
# print(car_2)
# print(car_2.color)
# print(car_2.body)

# print(MyCar)
# print(MyCar.color)



# class Cat:
#
#     def __new__(cls, *args, **kwargs): # метод, який насправді створює екземпляр класу
#         print("Creating Cat instance")
#         self = super().__new__(cls) # про функцію super() трохи пізніше
#         print(self)
#         return self # instance
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         print("Cat instance fields")
#         self.name = name
#         self.age = age
#         self.color = color
#
# cat = Cat('Barsik', 5, 'black')
# print(cat.age)



# class Cat(object):
# class Cat:
#     """Class for our cats"""
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         # print("Cat instance fields")
#         self.name = name
#         self.age = age
#         self.color = color
#
#
#     def cat_sound(self):
#         return "Meow"
#
#     def __str__(self):
#         return f"Hi my name is {self.name}, I'm {self.age} years old"
#
#     def __repr__(self):
#         return f"Cat {self.name}"
#
#
#
# cat = Cat('Barsik', 5, 'black')
# cat_2 = Cat('Tom', 6, 'black')
#
# class_list = [cat, cat_2]
# # print(class_list)
# # print(cat.age)
# # print(cat.cat_sound())
# print(cat)
# # print(cat_2)
# # print(cat.__doc__)
# # print(cat.__dir__())










# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Phone {self.brand} {self.model} {self.price}'
#
#
# class Laptop:
#     def __init__(self, brand, model, price):
#         # Важливо, щоб набір полів був схожим на інші класи, які зберігаються на складі
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Laptop {self.brand} {self.model} {self.price}'




# # Створимо кілька екземплярів класу Phone
# phone1 = Phone('Samsung', 'A52', 7000)
# # print(phone1)
# phone2 = Phone('Samsung', 'S11', 37000)
# phone3 = Phone('Samsung', 'A12', 4000)
# phone4 = Phone('Xiaomi', 'Redmi Note 11 ', 8700)
# phone5 = Phone('Xiaomi', '12 Lite', 17000)
# print(phone5)

# print(hash(phone1))


# class Warehouse:
#
#     def __init__(self, address):
#         self.address = address
#         self.storage = {}
#
#     def add_to_storage(self, item, value):
#         """ Метод додавання товару на склад """
#         self.storage[item] = value
#
#     def remove_from_storage(self, item):
#         """ Метод видалення товару зі складу """
#         value = self.storage.pop(item, None)
#         return value
#
#     def get_item_value(self, item):
#         """ Метод отримання кількості товару на складі """
#         return self.storage.get(item)
#
#     def get_total_value(self):
#         """ Метод отримання загальної вартості товару на складі """
#         total = 0
#         for key, cnt in self.storage.items():
#             total += key.price * cnt
#         return total
#
#     def __str__(self):
#         """ Метод виведення інформації про склад """
#         tmp = ''
#         for item, cnt in self.storage.items():
#             tmp += f'{str(item)}: {cnt} pcs. \n'
#         return f'Warehouse at {self.address} contains:\n{tmp} '


# wh = Warehouse('Kyiv, vul. Viskozna, 135')
# print(wh.get_total_value())  # На складі нічого немає
# #  Додамо на склад кілька телефонів і перевіримо деякі методи
# wh.add_to_storage(phone1, 40)
# wh.add_to_storage(phone2, 23)
# print(wh.get_total_value())
# print(wh.get_item_value(phone2))

# wh.add_to_storage(phone3, 4)
# wh.add_to_storage(phone4, 52)
# wh.add_to_storage(phone5, 22)
# print(wh.get_total_value())
# print(wh)
# # # Видалимо кілька телефонів і перевіримо інформацію по складу
# print(wh.remove_from_storage(phone2))
# print(wh.get_item_value(phone2))
# print(wh)



# #  Додамо на склад кілька ноутбуків
# notebook = Laptop('HP', 'ProBook 450', 35000)
# notebook1 = Laptop('HP', 'Laptop 15s-eq2054ur', 42000)
# wh.add_to_storage(notebook, 10)
# wh.add_to_storage(notebook1, 3)
# # print(wh.get_total_value())
# print(wh)


# def cat_sound():
#     return "Meow"

# class Cat(object):
# class Cat:
#     """Class for our cats"""
#     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
#         # print("Cat instance fields")
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f"Hi my name is {self.name}, I'm {self.age} years old"
#
#     def __repr__(self):
#         return f"Cat {self.name}"
#
#     @staticmethod
#     def cat_sound(name):
#         return f"{name} says Meow"


# cat = Cat('Barsik', 5, 'black')
# print(cat.cat_sound("Cat"))
# #
# print(Cat.cat_sound("Cat"))
# # print(cat_sound())

# from datetime import date
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # # Дозволяє обчислити дані, і повернути новий екземпляр класу, з цими даними
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#
#
# person1 = Person('Michael', 21)
# person2 = Person.from_birth_year('John', 1996)
# # person3 = person2.from_birth_year('mayank3', 2000)
#
# print(person1.age)
# print(person1.is_adult(person1.age))
# # print(person2.age)
# # print(person3.age)

# class Animal:
#     def __init__(self, name, food, color):
#             self.name = name
#             self.food = food
#             self.color = color
#
#     def animal_sound(self):
#         return "animal sounds like: "
#
#
# class Tiger(Animal):
#     def __init__(self, name, food, color, age):
#         super().__init__(name, food, color)
#         self.age = age
#
#     def animal_sound(self):
#         resp = super().animal_sound()
#         return resp + "Rrhhhh"
#
#
# tiger = Tiger("tiger", "meat", "orange", 9)
#
# print(tiger)
# print(tiger.name)
# print(tiger.animal_sound())