from new_group import Group_new
from new_student import Student
from MaxAmountException import MaxAmount_err

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

gr = Group_new('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except MaxAmount_err as err:
    print(f"[!] {err.get_exception_message()}!\n"
          f"[!] --> The student: {err.first_name} {err.name} to 11 on the list,"
          f" create a new group and add this student.")

print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
