from MaxAmountException import MaxAmount_err


class Group_new:

    def __init__(self, number):
        self._counter = None
        self.number = number
        self.group = set()

    def add_student(self, student):
        self._counter = 0
        for _ in self.group:
            self._counter += 1

        if self._counter == 10:
            raise MaxAmount_err(
                "Max Amount Students Exceeded", student.last_name, student.first_name)
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n{all_students}'