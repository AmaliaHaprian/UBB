from random import choice, randint

from src.domain.domain import Student


class Service:
    def __init__(self, repo):
        self._repo=repo
        self.generate_values()

    def add_student(self, student):
        """
        Adds a new student to the list of students
        :param student: the student object
        :return: None
        """
        self._repo.add(student)

    def filter_students(self, group):
        self._repo.filter(group)

    def get_students(self):
        return self._repo.get_all()

    def generate_values(self):
        names=["Anna", "John", "Emma", "Bob", "Mary", "Jane", "Lisa", "David", "Amy", "Eve"]

        for i in range(10):
            stud_id=i+1
            name=choice(names)
            group=randint(911,916)
            self.add_student(Student(stud_id, name, group))

    def undo_operation(self):
        self._repo.undo_last_op()