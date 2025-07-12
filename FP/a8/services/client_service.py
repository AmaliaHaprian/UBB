from faker import Faker

from src.domain.client import Client
from src.validators.errors import StringError
from src.validators.validator import Validator


class ClientService:
    def __init__(self,repo):
        self._repo = repo
        self._validator=Validator()
      #  self.generate_clients()

    def get(self, client_id):
        return self._repo[client_id]

    def add_client(self, client: Client):
        """
        Adds a new client
        :param client: the client entity to be added
        :return: None
        """
        if not self._validator.validate_string(client.name):
            raise StringError
        self._repo.add(client)

    def remove_client(self,client_id):
        """
        Removes a client
        :param client_id: the id of the client to be removed
        :return: None
        """

        self._repo.remove(client_id)

    def update_client(self,client_id,new_name):
        """
        Updates a client
        :param client_id: the id of the client to be updated
        :param new_name: the new name of the client
        :return: None
        """

        self._repo.update(client_id,new_name)

    def get_clients(self):
        return self._repo.get_all()

    def search_id(self,client_id):
        return self._repo.search_id(client_id)

    def search_name(self,client_name):

        return self._repo.search_by_name(client_name)

    def last_client(self):
        return self._repo.get_last_client()







    def generate_clients(self):

        fake = Faker()

        for i in range(100, 121):
            self.add_client(Client(i, fake.name()))
