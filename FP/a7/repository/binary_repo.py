import pickle

from pdoc import pdoc

from src.domain.domain import Student
from src.repository.memo_repo import MemoryRepo, RepositoryError


class BinaryRepo(MemoryRepo):
    """
    The repository class that stores the data in a binary file
    """

    def __init__(self, file_name: str = "stud_binary_repo.bin"):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _load(self):
        #try:
         #   fin = open(self._file_name, "x")
          #  fin.close()
        #except FileExistsError:
         #   with open(self._file_name, "rb") as fin:
            #    text = pickle.load(fin)

        try:
            fin=open(self._file_name, "rb")
            text=pickle.load(fin)
        except EOFError:
            return

        for student in text:
            if student not in text:
                super().add(student)

    def _save(self):
        with open(self._file_name, "wb") as fout:
            pickle.dump(self._data, fout)


    def add(self, student: Student):
        """
        Adds a new student to the list of students and saves it in the binary file
        :param student: the student object
        :return: None
        """
        super().add(student)
        self._save()

    def filter(self, group):
        super().filter(group)
        self._save()

    def undo_last_op(self):
        super().undo_last_op()
        self._save()

if __name__ == "__main__":
    #repo = BinaryRepo()
    #repo.add(Student(1, "anna", 914))
    #print(len(repo))
    #test_binary_repo()
    f = open("binary_doc.html", "wt")
    f.write(pdoc("binary_repo.py", ""))
    f.close()
