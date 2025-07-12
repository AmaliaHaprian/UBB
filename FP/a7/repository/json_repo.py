import json
from src.domain.domain import Student
from src.repository.memo_repo import MemoryRepo


class JsonRepo(MemoryRepo):
    def __init__(self, file_name="stud.json"):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _load(self):
        try:
            fin = open(self._file_name, "x")
            fin.close()
        except FileExistsError:
            with open(self._file_name, "rt") as fin:
                self._data = json.load(fin)
        array=[]
        for stud in self._data:
            split_text=stud.split()
            stud_id=int(split_text[1])
            name=split_text[3]
            group=int(split_text[5])
            array.append(Student(stud_id, name, group))
        return array

        #for student in self._data.values():
         #   if student.stud_id not in self._data:
          #      super().add(student)

    def _save(self, array: list):
        with open(self._file_name, "wt") as fout:
            for i in range(len(array)):
                json.dump(str(array[i]), fout)

        fout.close()

    def add(self, student: Student):
        super().add(student)
        self._save()

    def filter(self, group):
        super().filter(group)
        self._save()

    def undo_last_op(self):
        super().undo_last_op()
        self._save()

if __name__ == "__main__":
    repo=JsonRepo()
    repo.add(Student(1, "anna", 914))
    print(len(repo))