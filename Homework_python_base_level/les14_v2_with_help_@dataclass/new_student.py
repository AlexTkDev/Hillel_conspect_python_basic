from new_human import Human_new
from dataclasses import dataclass


@dataclass
class Student(Human_new):
    record_book: str

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (self.record_book == other.record_book and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.age == other.age and
                self.gender == other.gender)

    def __str__(self):
        return (f'{self.record_book}: {self.first_name} {self.last_name},'
                f' age is {self.age}, gender is {self.gender}\n')