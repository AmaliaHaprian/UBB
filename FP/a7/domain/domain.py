class Student(object):
    def __init__(self, stud_id, name:str, group):
        """
        Creates an object student with an unique integer as student_id, name and group
        :param stud_id: unique integer
        :param name: string
        :param group: a positive integer
        """
        if group<=0 or stud_id<=0:
            raise ValueError("Group must be a positive integer")
        if type(name)!=str or type(stud_id)!=int or type(group)!=int:
            raise ValueError("Invalid type")
        self.__stud_id = stud_id
        self.__name = name
        self.__group = group

    @property
    def stud_id(self):
        return self.__stud_id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @stud_id.setter
    def stud_id(self, stud_id):
        self.__stud_id = stud_id

    @name.setter
    def name(self, name):
        self.__name = name

    @group.setter
    def group(self, group):
        self.__group = group

    def to_str(self):
        return "ID: " + str(self.__stud_id) + " Name: " + self.__name + " Group: " + str(self.__group)

if __name__ == "__main__":
    student=Student(1, "Anna", 914)
    student.group = 915
    print(student.to_str())