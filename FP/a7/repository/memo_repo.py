import copy

from pdoc import pdoc

from src.domain.domain import Student
class RepositoryError(Exception):
    pass

class MemoryRepo():
    """
    The repository class that stores the data in memory
    """

    def __init__(self):
        self._history=[]
        self._data={}

    def add(self, student: Student):
        """
        Add a new student to the list of students
        :param student: an object of type Student
        :return: None
        """
        if student.stud_id in self._data:
            raise RepositoryError("Duplicate student ID error")
        self._data[student.stud_id]=student
        self._history.append(copy.deepcopy(self._data))

    def get_all(self):
        return list(self._data.values())

    def filter(self, group):
        """
        Filters the students by group
        :param group: the group to be deleted
        :return: None
        """
        filtered={}
        for stud in self._data.values():
            if stud.group!=int(group):
                filtered[stud.stud_id]=stud
        self._data=filtered.copy()
        self._history.append(copy.deepcopy(self._data))

    def undo_last_op(self):
        """
        Undoes the last operation performed on the list of students
        :return: None
        """
        if len(self._history)==11:
            self._history.pop()
            self._data={}
            for stud in self._history:
                self._data.update(stud)


        elif len(self._history)>11:
            self._history.pop()
            self._data = self._history[-1]
        else:
            raise RepositoryError("Error! Nothing to undo anymore. This is the default list of students")


    def __len__(self):
        return len(self._data)

    def to_str(self):
        return str(self._data)

if __name__=="__main__":

    f=open("memory_doc.html", "wt")
    f.write(pdoc("memo_repo.py", ""))
    f.close()