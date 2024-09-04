# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.gender}, {self.age} years old)\n"
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         self.record_book = record_book
#         super().__init__(gender, age, first_name, last_name)
#
#     def __str__(self):
#         resp = super().__str__()
#         return f"Student {self.record_book}: " + resp
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student is not None:
#             self.group.remove(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = ''
#         for student in self.group:
#             all_students += str(student)
#
#         return f'Number:{self.number}\n{all_students} '
#
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st3 = Student('Male', 31, 'Michael', 'Jacson', 'AN143')
# st4 = Student('Female', 26, 'Marilyn', 'Monroe', 'AN144')
#
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# gr2 = Group('PD2')
# gr2.add_student(st3)
# gr2.add_student(st4)
# print(gr)
# print(gr2)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'
#
# gr.delete_student('Taylor')
# gr2.delete_student('Jacson')
# print(gr)  # Only one student
# print(gr2)  # Only one student
#
# gr.delete_student('Taylor')  # No error!



# class Counter:
#
#    def __init__(self, current=1, min_value=0, max_value=10):
#        self.current = current
#        self.min_value = min_value
#        self.max_value = max_value
#
#    def set_current(self, start):
#        self.current = start
#
#    def set_max(self, max_max):
#         self.max_value = max_max
#
#    def set_min(self, min_min):
#        self.min_value = min_min
#
#    def step_up(self):
#        if self.current >= self.max_value:
#             raise ValueError(f"Досягнуто максимуму! Counter = {self.current}")
#        else:
#            self.current += 1
#
#    def step_down(self):
#        if self.current <= self.min_value:
#         raise ValueError(f"Досягнуто мінімуму! Counter = {self.current}")
#        else:
#            self.current -= 1
#
#    def get_current(self):
#        return self.current
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e) # Досягнуто максимуму
# assert counter.get_current() == 10, 'Test2'
#
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e) # Досягнуто мінімуму
# assert counter.get_current() == 7, 'Test4'
















# class Cat:
#     def __init__(self, name, _age, __color):
#         self.name = name
#         self.age = _age
#         self.color = __color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.name)
# print(cat.type) # Звернення до поля, якого немає












# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattr__(self, atr_name):
#         print(atr_name)
#         return None # pass
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.type) # Звернення до поля, якого немає
# print(cat.name)





# KeyError ніколи не спрацює, тому що self.__dict__[attr]
# викличе __getattribute__(self, attr) і це призведе до зациклювання
# class Foo(object):
#     def __init__(self, a):
#         self.a = 1
#     # Викликається для пошуку всіх атрибутів
#     def __getattribute__(self, attr):
#         try:
#             return self.__dict__[attr]# Спроба отримати значення за ключем
#         except KeyError:
#             return 'default'




# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattribute__(self, atr_name):
#         """ Робити перехоплення винятку у цьому методі, не зовсім коректно.
#         Більш правильний підхід - реалізувати роботу з полями,
#         яких немає, у методі гетатр"""
#         try:
#             return object.__getattribute__(self, atr_name)
#             # return super().__getattribute__(self, atr_name)
#         except AttributeError:
#             if atr_name == "type":
#                 return "Home Cat"
#             print(atr_name)
#             return None
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.type) # Звернення до поля, якого немає
# print(cat.name)
# # print(cat.okras)







# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattr__(self, atr_name):
#         if atr_name == "type":
#             return "Home Cat"
#         return None
#
#     def __getattribute__(self, atr_name):
# #         if atr_name == 'type':
# #         print(f'----{atr_name}----')
#         return object.__getattribute__(self, atr_name)
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.type) # Звернення до поля, якого немає
# print(cat.name)
# print(cat.x) # Звернення до поля, якого немає












# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattr__(self, atr_name):
#         if atr_name == "type":
#                 return "Home Cat"
#         print(atr_name)
#         return "11"
#
#     def __getattribute__(self, atr_name):
#         return object.__getattribute__(self, atr_name)
#
#     def __setattr__(self, attr_name, attr_value):
#         print("set field -> ", attr_name)
#         # self.attr_name = attr_value #Нескінченна рекурсія,
#         # спроба встановити значення для поля,
#         # знову викличе __setattr__(self, attr_name, attr_value)
#         self.__dict__[attr_name] = attr_value
#
# cat = Cat('Barsik', 3, 'black')

# cat.type = "Devil"
# print(cat.type)






# import math
# setattr(math, 'piii', 1254)
# print(math.piii)


# cat.name = 'Bob'
# dct = {'name': "Voland", "age": 45}
# for key in dct:
#     # Отримаємо значення полів об'єкта
#     print(getattr(cat, key))
#
#
# for key, val in dct.items():
#     # Встановимо нові значення для полів об'єкта
#     setattr(cat, key, val)
# print(cat)









# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattr__(self, atr_name):
#         if atr_name == "type":
#             return "Home Cat"
#         print(atr_name)
#         return "11"
#
#     def __getattribute__(self, atr_name):
#         return object.__getattribute__(self, atr_name)
#
#     def __setattr__(self, attr_name, attr_value):
#         print("set field -> ", attr_name)
#         self.__dict__[attr_name] = attr_value
#
#     def __delattr__(self, attr_name):
#         # Видаляємо поле з внутрішньої структури об'єкта
#         print("remove field ", attr_name)
#         del self.__dict__[attr_name]
#
# cat = Cat('Barsik', 3, 'black')
# cat.type = "Devil"
# del cat.type
#
# print(cat.type)









# property


# class Cat:
#     def __init__(self, _name, age):
#         self.__name = _name   # захищене поле
#         self.age = age
#
#     def get_name(self): # Метод для читання
#         print("call get name")
#         return self.__name
#
#     def set_name(self, name_value): # Метод для запису
#         print("call set name")
#         self.__name = name_value
#
#     def del_name(self): # Метод видалення
#         print("call remove name")
#         del self.__name
#
#     # Створення властивості name
#     name = property(get_name, set_name, del_name, " Cat name")
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}]"
#         return msg.format(self.name, self.age)
#
# cat1 = Cat("Vaska", 6)
# cat1.name = "Barsic"
# print(cat1.name)
# print(cat1)






# class Cat:
#     def __init__(self, _name, age):
#         self.__name = _name
#         self.age = age
#
#     name = property() # Створення властивості name без методів контролю
#
#     @name.getter
#     def name(self):
#         print("call get name")
#         return self.__name
#
#     @name.setter
#     def name(self, name_value):
#         print("call set name")
#         self.__name = name_value
#
#     @name.deleter
#     def name(self):
#         print("call remove name")
#         del self.__name
#
# cat = Cat('Barsik', 3)
# print(cat.name )
# cat.name =  "Devil"
# del cat.name














# class Cat:
#     def __init__(self, _name, age):
#         self.__name = _name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     # @name.setter
#     # def name(self, value):
#     #     # self.__name = value
#     #     raise
#
#
# cat = Cat('Barsik', 3)
# print(cat.name)
# cat.name = "Tom"
# print(cat.name)



























# Перетворення функції (методу) у звичайне поле
# class Human:
#
#     def __init__(self, last_name, first_name, patronymic, gender, age, height, weight):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.patronymic = patronymic
#         self.gender = gender
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def show_inform(self):
#         full_name = f'Full Name: {self.full_name}\n'
#         gender_age = f'Gender: {self.gender}\nAge: {self.age}\n'
#         height_weight = f'Height: {self.height} cm\nWeight: {self.weight} kg'
#         all_info = full_name + gender_age + height_weight
#         return all_info
#
#     @property  #cashed_property
#     def full_name(self):
#         # Перетворення функції (методу) у звичайне поле
#         return f'{self.last_name} {self.first_name} {self.patronymic}'
#
#     @property
#     def short_full_name(self):
#         return f'{self.last_name} {self.first_name[0].title()}.{self.patronymic[0].title()}.'
#
# h = Human('Лучко', 'Петро', 'Петрович', 'male', 25, 185, 91)
#
# print(h.full_name)
# print(h.short_full_name)
# print(h.last_name)






# Дескриптори


# class MyDescriptor:
#     def __init__(self, n):
#         self.n = n
#
#     def __get__(self, instance_self, instance_class):
#         print(self)
#         print(instance_self)
#         print(instance_class)
#         return self.n * instance_self.p
#
#
# class Box:
#     volume = MyDescriptor(2)  # Створення поля керованого дескриптором
#
#     def __init__(self, x, y, z):
#         self.p = x * y * z
#
#
# box1 = Box(1, 2, 3)
# print(box1.volume)
# # Дескриптор буде перезаписано новим значенням тому, що не реалізовано метод встановлення значення дескриптора
# box1.volume = 4
# print(box1.volume)






# class ProtectedField:
#     def __init__(self, field):
#         self.field = field
#
#     def __get__(self, instance_self, instance_class):
#         field = f'_{instance_class.__name__}{self.field}'  # _Cat__name
#         return getattr(instance_self, field)
#
#
# class Cat:
#     name = ProtectedField('__name')
#     age = ProtectedField('__age')
#
#     def __init__(self, _name, _age):
#         self.__name = _name
#         self.__age = _age
#
#
# cat = Cat('Barsik', 3)
# # print(cat.__name )  # буде помилка
# print(cat._Cat__name ) # Доступ до захищеного поля
# # Доступ до захищених полів через дескриптор
# print(cat.name)
# print(cat.age)






# class MyDescriptor:
#     def __init__(self, n):
#         self.n = n
#
#     def __get__(self, instance_self, instance_class):
#         return self.n * instance_self.p
#
#     def __set__(self, instance_self, value):
#         raise AttributeError("field is read-only")
#
#
# class Box:
#     volume = MyDescriptor(2)
#     def __init__(self, x, y, z):
#         self.p = x * y * z
#
# box1 = Box(1, 2, 3)
# print(box1.volume)
# box1.volume = 50 # AttributeError: field is read-only


# метод сет для дескриптора ProtectedField
# class ProtectedField:
#     def __init__(self, field):
#         self.field = field
#
#     def __get__(self, instance_self, instance_class):
#         field = f'_{instance_class.__name__}{self.field}'  # _Cat__name
#         return getattr(instance_self, field)
#
#     def __set__(self, instance_self, value):
#         # instance_class у метод __set__ не передається, тому отримуємо його з об'єкта
#         instance_class = instance_self.__class__
#         field = f'_{instance_class.__name__}{self.field}' # _Cat__name
#         setattr(instance_self, field, value)
#
#     # def __set__(self, instance_self, value):
#     #     raise AttributeError("cannot set field")
#
#
# class Cat:
#     name = ProtectedField('__name')
#     age = ProtectedField('__age')
#
#     def __init__(self, _name, _age):
#         self.__name = _name
#         self.__age = _age

#
# cat = Cat('Barsik', 3)
# print(cat.name)


















# class ProtectedField:
    #
    # def __init__(self, field):
    #     self.field = field
    #
    # def __get__(self, instance_self, instance_class):
    #     field = f'_{instance_class.__name__}{self.field}'  # _Cat__name
    #     return getattr(instance_self, field)
    #
    # def __set__(self, instance_self, value):
    #     # instance_class у метод __set__ не передається, тому отримуємо його з об'єкта
    #     instance_class = instance_self.__class__
    #     field = f'_{instance_class.__name__}{self.field}'
    #     setattr(instance_self, field, value)
    #
    # def __delete__(self, instance_self):
    #     instance_class = instance_self.__class__
    #     field = f'_{instance_class.__name__}{self.field}'
    #     delattr(instance_self, field)

    # def __delete__(self, instance_self):
    #     raise AttributeError("cannot delete field")

# class Cat:
#     name = ProtectedField('__name')
#     age = ProtectedField('__age')
#
#     def __init__(self, _name, _age):
#         self.__name = _name
#         self.__age = _age
#
#
# cat = Cat('Barsik', 3)
# print(cat.name)
# del cat.name  # AttributeError: cannot delete field













# # Приклад реалізації дескриптора для поля, яке має бути більше за 0
# class PositiveValue:
#
#     def __init__(self):
#         self.val = None
#
#     def __get__(self, instance_self, instance_class):
#         return self.val
#
#     def __set__(self, instance_self, value):
#         if value < 0:
#             raise ValueError('Value must be greater than zero')
#         self.val = value
#
#
# class Box:
#     x = PositiveValue()
#     y = PositiveValue()
#     z = PositiveValue()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# box = Box(1, 2, 3)
# print(box.x)
# box.x = -1  # ValueError
# box = Box(1, 2, -3)  # ValueError








# Ітератори та ітераційний протокол





# class UserSequence:
#     """Реалізація послідовності квадратів чисел
#     """
#     def __init__(self, number):
#         self.number = number
#
#     def __getitem__(self, index):
#         if index < self.number:
#             return index ** 2 # поверне квадрат значення index
#         else:
#             raise IndexError
#
#     def __len__(self):
#         return self.number


# seq = UserSequence(10)
# # Отримуємо елементи послідовності у циклі
# for i in range(len(seq)):
#     print(seq[i])




# # Можемо отримати елемент послідовності за індексом
# print(seq[9])
#
# # # Можемо отримати всі елементи послідовності у вигляді списку
# print(list(seq))
# # Але при цьому для нашої послідовності не працюють зрізи
# print(seq[2: 4])





# a = [5, 6, 7, 8, 9]
# b = a[0: 3]
# print(b)

# slice_ = slice(0, 3)
# print(slice_)  # 0
# print(slice_.start)  # 0
# print(slice_.stop)  # 3
# print(slice_.step)  # None
# print(a[slice_])
# print(a[0:3])
#
# print(a[slice(1, None)])
# print(a[1:])
# # [6, 7, 8, 9]
# print(a[slice(None, -1)])
# print(a[:-1])
# # [5, 6, 7, 8]
# print(a[slice(None, None, 2)])
# print(a[::2])
# # [5, 7, 9]


# class UserSequence:
#     """ Реалізація послідовності квадратів чисел, що підтримує звернення за допомогою зрізів"""
#
#     def __init__(self, number):
#         self.number = number
#
#     def __getitem__(self, index):
#         # перевірка того, що індекс це об'єкт зрізу
#         if isinstance(index, slice):
#             # перевірка коректності значень об'єкт зрізу
#             if index.start and index.start < 0:
#                 raise IndexError
#             elif index.stop and index.stop > self.number:
#                 raise IndexError
#             result = []
#             # встановлення конкретних значень зрізу, якщо такі не були задані
#             start = 0 if index.start is None else index.start
#             stop = self.number if index.stop is None else index.stop
#             reverse = False
#             # якщо значення кроку від'ємне, значить буде перевернута послідовність
#             if index.step and index.step < 0:
#                 reverse = True
#                 step = index.step * (-1)
#             else:
#                 step = 1 if index.step is None else index.step
#             # процес формування послідовності
#             for i in range(start, stop, step):
#                 result.append(i ** 2)
#             # перевертаємо послідовність, якщо reverse = True
#             return list(reversed(result)) if reverse else result
#
#         if isinstance(index, int):
#             if index < self.number:
#                 return index ** 2
#             else:
#                 raise IndexError
#         raise TypeError
#
#     def __len__(self):
#         return self.number














# iter(), next()

#
# a = "Hello"
# b = a.__iter__()
# print(type(b))
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())




# class Goods:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"Goods [name = {self.name}, price = {self.price}]"
#
#
# class Basket:
#     """ У цій реалізації не можна пройти по елементам Кошика в циклі """
#     def __init__(self, user):
#         self.user = user
#         self.purchase_list = list()
#
#     def add_purchase(self, purchase):
#         self.purchase_list.append(purchase)
#
#     def __str__(self):
#         result = f"User: {self.user}\n"
#         for purchase in self.purchase_list:
#             result += str(purchase)+"\n"
#         return result
#
# basket = Basket("Alexander_Ts")
#
# a = Goods("Apple", 35)
# b = Goods("Milk", 50)
#
# basket.add_purchase(a)
# basket.add_purchase(b)
#
# print(basket)
# for purchase in basket:
#     print(purchase)













# class BasketIterator:
#     """ Клас ітератор, який знає як обробляти наповнення Кошика,
#     щоб віддавати по одному елементу при кожному запиті
#     """
#
#     def __init__(self, purchase_list):
#         """При ініціалізації отримує список товарів
#         і встановлює значення індексу 0"""
#         self.purchase_list = purchase_list
#         self.index = 0
#
#     def __next__(self):
#         """ Якщо значення індексу не виходить за межі розміру
#         списку, надаємо елемент Кошика.
#         В іншому випадку - викликаємо виняток"""
#         if self.index < len(self.purchase_list):
#             res = self.purchase_list[self.index]
#             self.index = self.index + 1
#             return res
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self


# class Basket:
#     def __init__(self, user):
#         self.user = user
#         self.purchase_list = list()
#
#     def add_purchase(self, purchase):
#         self.purchase_list.append(purchase)
#
#     def __str__(self):
#         result = f"User: {self.user}\n"
#         for purchase in self.purchase_list:
#             result += str(purchase)+"\n"
#         return result
#
#     def __iter__(self):
#         """Повертаємо екземпляр класу Ітератора"""
#         return BasketIterator(self.purchase_list)






# basket = Basket("Alexander_Ts")
#
# a = Goods("Apple", 35)
# b = Goods("Milk", 50)
#
# basket.add_purchase(a)
# basket.add_purchase(b)

# for purchase in basket:
#     print(purchase)

# # print('**' * 6)
# c = Goods("Oil", 100)
# basket.add_purchase(c)

# for purchase in basket:
    # print(purchase)

# print(basket)
# it = iter(basket)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# itr = iter(basket)
# # print(itr)
# while True:
#     try:
#         purchase = next(itr)
#         print(purchase)
#     except StopIteration:
#         break
#
# for i in basket:
#     print(i)






