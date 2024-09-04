from ERROR_MaxAmountException import MaxAmountException, MAX_STUDENT_ERROR_MESSAGE


class Group:
    MAX_STUDENT = 10

    def __init__(self, number):
        self._counter = None
        self.number = number
        self.group = set()

    def add_student(self, student):
        self._counter = 0
        for _ in self.group:
            self._counter += 1

        if self._counter == self.MAX_STUDENT:
            raise MaxAmountException(MAX_STUDENT_ERROR_MESSAGE,
                                     student.last_name, student.first_name)
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            return self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n{all_students}'