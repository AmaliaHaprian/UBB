from src.domain.domain import Student
from src.repository.binary_repo import BinaryRepo
from src.repository.memo_repo import MemoryRepo, RepositoryError
from src.repository.text_repo import TextRepo
from src.services.services import Service


class Test:
    def __init__(self,repo):
        self.student_service=Service(repo)

    def test_generate(self):
        assert len(self.student_service.get_students())==10

    def test_add(self):
        self.student_service.add_student(Student(11, "ana", 918))
        assert len(self.student_service.get_students())==11
        try:
            self.student_service.add_student(Student(11, "ana", 918))
            assert False
        except RepositoryError:
            assert len(self.student_service.get_students())==11

    def test_filter(self):
        self.student_service.filter_students(918)
        assert len(self.student_service.get_students())==10

    def test_undo(self):
        self.student_service.add_student(Student(11, "John", 913))
        assert len(self.student_service.get_students())==11
        self.student_service.undo_operation()
        assert len(self.student_service.get_students())==10

    def test_all(self):
        self.test_generate()
        self.test_add()
        self.test_filter()
        self.test_undo()

if __name__=="__main__":
    repo=MemoryRepo()
    test=Test(repo)
    test.test_all()

    repo=BinaryRepo()
    test=Test(repo)
    test.test_all()

    repo=TextRepo()
    test=Test(repo)
    test.test_all()