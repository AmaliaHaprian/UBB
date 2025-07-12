from src.domain.client import Client
from src.repository.book_repository.book_memo_repo import EmptyInputError, InputError


class ClientRepositoryError(Exception):
    pass
class DuplicateClientIDError(ClientRepositoryError):
    pass
class ClientIDNotFoundError(ClientRepositoryError):
    pass


class ClientRepositoryIterator():
    def __init__(self, data):
        self.__data=data
        self.__pos=-1
    def __next__(self):
         self.__pos +=1
         if len(self.__data)==self.__pos:
             raise StopIteration()
         return self.__data[self.__pos]

class ClientMemoRepo():
    def __init__(self):
        self._data={}

    def add(self,client:Client):
        """
        The function add a new client to the repository. If there already is a client with such id, it raises an error
        :param client: the client entity
        :return: None
        """

        if int(client.client_id) in self._data:
            raise DuplicateClientIDError("Duplicate client id")
        if len(client.name)==0:
            raise EmptyInputError('Field cannot be empty')
        if len(client.name)<3:
            raise InputError('Field name should be at least 3 characters long')
        self._data[client.client_id] = client

    def remove(self,client_id):
        """
        The function removes a client from the repository. If there is no such client, it raises an error.
        :param client_id: the id of the client to remove
        :return: the modifies list of clients
        """

        if client_id not in self._data:
            raise ClientIDNotFoundError("Client id not found")
        return self._data.pop(client_id)

    def update(self,client_id, new_name):
        """
        The function updates a client in the repository. If there is no such client, it raises an error.
        :param client_id: the id of the client to update
        :param new_name: the new name of the client
        :return: None
        """

        if client_id not in self._data:
            raise ClientIDNotFoundError("Client id not found")
        if len(new_name)==0:
            raise EmptyInputError('Field cannot be empty')
        if len(new_name)<3:
            raise InputError('Field name should be at least 3 characters long')
        else:
            self._data[client_id].name = new_name

    def get_last_client(self):
        return sorted(self._data.keys())[-1]

    def get_all(self):
        return list(self._data.values())

    def search_by_client_id(self,search_client_id):
        for client_id in self._data:
            if client_id == search_client_id:
                return self._data[client_id]

    def search_by_name(self, search_client_name):
        if len(search_client_name)==0:
            raise EmptyInputError('Field cannot be empty')
        filtered=[]
        for client_id in self._data.keys():

            if search_client_name.lower() in self._data[client_id].name.lower():
                filtered.append(self._data[client_id])
        return filtered

    def __iter__(self):
        return ClientRepositoryIterator(list(self._data.values()))

    #def __getitem__(self, key):
     #   if key not in self._data:
      #      return None
       # return self._data[key]
