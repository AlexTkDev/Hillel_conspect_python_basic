import numbers


# ------ option 1 ----------
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.get_square() == other.get_square()
#
#     def __add__(self, other):
#         # _temp_width = 1
#         # _temp_height = self.get_square() + other.get_square()
#         # return Rectangle(_temp_width, _temp_height)
#
#         # or
#         # return Rectangle(1, self.get_square() + other.get_square())
#
#         # or
#         combined_area = self.width * self.height + other.width * other.height
#         return Rectangle(combined_area ** 0.5, combined_area / (combined_area ** 0.5))
#
#     def __mul__(self, n):
#         # _temp_width = self.width * n
#         # _temp_height = self.height
#         # return Rectangle(_temp_width, _temp_height)
#
#         # or
#         return Rectangle(self.width, n * self.height)
#
#     def __str__(self):
#         return f"Rectangle [width= {self.width},height= {self.height}, square= {self.get_square()}]"
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
# #
# r3 = r1 + r2
# print("R3 -->", r3)
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# print("R4 -->", r4)
# assert r4.get_square() == 32, 'Test4'
# ------ option 2 ----------


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square == other.get_square

    def __add__(self, other):
        combined_area = self.get_square + other.get_square
        return Rectangle(combined_area ** 0.5, combined_area / (combined_area ** 0.5))

    def __mul__(self, n):
        return Rectangle(self.width, n * self.height)

    def __str__(self):
        return f"Rectangle [width={self.width}, height={self.height}, area={self.get_square}]"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square == 8, 'Test1'
assert r2.get_square == 18, 'Test2'

r3 = r1 + r2
print("R3 -->", r3)
assert r3.get_square == 26, 'Test3'

r4 = r1 * 4
print("R4 -->", r4)
assert r4.get_square == 32, 'Test4'
