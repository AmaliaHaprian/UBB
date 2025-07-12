from pdoc import pdoc

from src.domain.domain import Student
from src.repository.memo_repo import MemoryRepo


class TextRepo(MemoryRepo):
    """
    The repository class that stores the data in a text file
    """

    def __init__(self, file_name="stud.txt"):
        super().__init__()
        self._file_name=file_name
        self._load()
    def _load(self):
        lines=[]
        #fin=open(self._file_name, "rt")
        #lines=fin.readlines()
        #fin.close()

        #for line in lines:
           # current_line=line.split(",")
           # new_student=Student(int(current_line[1].strip()),current_line[3].strip(),int(current_line[5].strip()))
           # super().add(new_student)


        with open(self._file_name, "rt") as fin:
            line=fin.readline()
            while line:
                current_line=line.split(",")
                if len(current_line)==6:
                    new_student=Student(int(current_line[1].strip()),current_line[3].strip(),int(current_line[5].strip()))
                    super().add(new_student)
                line=fin.readline()
        fin.close()

    def _save(self):
        #fout=open(self._file_name, "wt")
        #for student in self.get_all():
        #    fout.write(student.to_str() + "\n")

        with open(self._file_name, "wt") as fout:
            for student in self.get_all():
                fout.write(student.to_str() +"\n")
        fout.close()

    def add(self, student: Student):
        """
        Adds a new student to the list of students and saves it in the text file
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

if __name__=="__main__":
    #repo=TextRepo()
    #repo.add(Student(1, "anna", 914))
    #repo.add(Student(2, "anna", 914))
    #print(len(repo))
    f = open("text_doc.html", "wt")
    f.write(pdoc("text_repo.py", ""))
    f.close()