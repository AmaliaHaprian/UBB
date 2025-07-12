from src.domain.domain import Student
from src.repository.binary_repo import BinaryRepo
from src.repository.json_repo import JsonRepo
from src.repository.memo_repo import MemoryRepo, RepositoryError
from src.repository.text_repo import TextRepo
from src.services.services import Service


class UI:
    def __init__(self,repo):
        self._student_service=Service(repo)

    def add_stud_ui(self):
        stud_id=input("Please enter student id:")
        name=input("Please enter student name:")
        group=input("Please enter student group:")

        #self._memo_repo.add_student(Student(stud_id,name,group))

    def display_students_ui(self, repo):
        for stud in repo:
            print(stud.to_str())

    def filter_students_ui(self):
        group=input("Please enter the group you want to remove")
        #self._memo_repo.filter_students(group)

    @staticmethod
    def print_menu(self):
        print("""
        1. Add Student
        2. Display Students
        3. Filter Students
        4. Undo""")

    def start(self):
        #self._memo_repo = MemoryRepo()
        while True:
            UI.print_menu(self)
            choice=input("Enter your choice:")
            if choice=="1":
                try:
                    stud_id = int(input("Please enter student id:"))
                    name = input("Please enter student name:")
                    group = int(input("Please enter student group:"))
                    self._student_service.add_student(Student(stud_id, name, group))
                except ValueError as ve:
                    print(ve)
                except RepositoryError as re:
                    print(re)
                except TypeError as te:
                    print(te)
            elif choice=="2":
                self.display_students_ui(self._student_service.get_students())
            elif choice=="3":
                group = input("Please enter the group you want to remove:")
                self._student_service.filter_students(group)
            elif choice=="4":
                try:
                    self._student_service.undo_operation()
                except RepositoryError as re:
                    print(re)
            else:
                print("Invalid choice")

#def start_all():
 #   repo=MemoryRepo()
  #  ui=UI (repo)
   # ui.start()