class Client:
    def __init__(self, client_id:int, name:str):
        self.__client_id = client_id
        self._name = name

    @property
    def client_id(self):
        return self.__client_id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def __str__(self):
        return f"Client with id={self.client_id}  is {self.name}"
    def __repr__(self):
        return str(self)
