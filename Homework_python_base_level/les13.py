# # -------------------------- EX 1 -------------------------
#
#
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}, age is {self.age}, gender is {self.gender}'
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         rsp = super().__str__()
#         return f'{self.record_book}: {rsp}\n'
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
#             return self.group.remove(student)
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
#             all_students += student.__str__()
#         return f'Number:{self.number}\n{all_students} '
#
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'
# #
# gr.delete_student('Taylor')
# print(gr)  # Only one student
# #
# gr.delete_student('Taylor')  # No error!
#
#
# # # -------------------------- EX 2 -------------------------
#
# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         self.current = start
#
#     def set_max(self, max_max):
#         self.max_value = max_max
#
#     def set_min(self, min_min):
#         self.min_value = min_min
#
#     def step_up(self):
#         if self.current == self.max_value:
#             raise ValueError(f"Reached maximum value = {self.max_value}")
#         else:
#             self.current += 1
#         return self.current
#
#     def step_down(self):
#         if self.current == self.min_value:
#             raise ValueError(f"Reached minimum value = {self.min_value}")
#         else:
#             self.current -= 1
#         return self.min_value
#
#     def get_current(self):
#         return self.current
#
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
#     print(e)  # Досягнуто максимуму
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e)  # Досягнуто мінімуму
# assert counter.get_current() == 7, 'Test4'


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        return Box.__add__(self, other)

    def __radd__(self, other):
        return Box.__add__(self, other)

    def __add__(self, other):
        if isinstance(other, Box):
            print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, numbers.Real):
            return Box(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Box(self.x * other, self.y * other, self.z * other)
        else:
            return NotImplemented

    @staticmethod
    def volume(box):
        return box.x * box.y * box.z

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.volume(self) == self.volume(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume(self) > self.volume(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Box):
            return not self > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Box):
            return any((self > other, self == other))
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Box):
            return any((self < other, self == other))
        return NotImplemented

    def __ne__(self, other):
        return not self == other


box_a = Box(1, 2, 3)
box_b = Box(1, 2, 3)
print(box_a >= box_b)
box_c = box_a + box_b
print(box_c >= box_b)
print(box_a <= box_b)
all([1, 0, True])
any([1, 0, True])
