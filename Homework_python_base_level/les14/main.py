from group import Group
from add_student import Student
from ERROR_MaxAmountException import MaxAmountException

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 45, 'Ed', 'Mon', 'AN146')
st4 = Student('Male', 70, 'Tom', 'Fonz', 'AN142')
st5 = Student('Male', 20, 'Yota', 'Cats', 'AN145')
st6 = Student('Male', 44, 'Tonny', 'Messi', 'AN147')
st7 = Student('Female', 23, 'Alex', 'Smith', 'AN148')
st8 = Student('Male', 22, 'Oz', 'Rider', 'AN149')
st9 = Student('Female', 34, 'Leyla', 'Fill', 'AN148')
st10 = Student('Male', 32, 'Sam', 'Daytona', 'AN155')
st11 = Student('Male', 33, 'Ros', 'Geller', 'AN1455')
list_student = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, ]

gr = Group('PD1')
try:
    for student in list_student:
        gr.add_student(student)

except MaxAmountException as err:
    print(f"[!] {err.get_exception_message()}!\n"
          f"[!] --> The student: {err.first_name} {err.name} to 11 on the list,"
          f" create a new group and add this student.")

print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
