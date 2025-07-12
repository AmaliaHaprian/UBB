from faker import Faker

from src.domain.client import Client
from src.services.rental_service import RentalService
from src.services.undo_service import UndoService, FunctionCall, Operation, CascadeOperation
from src.validators.errors import StringError
from src.validators.validator import Validator


class ClientService:
    def __init__(self,repo, undo_service:UndoService, rental_service: RentalService):
        self._repo = repo
        self._validator=Validator()
        self._rental_service=rental_service
        self._undo_service=undo_service
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

        function_undo=FunctionCall(self._repo.remove,client.client_id)
        function_redo=FunctionCall(self._repo.add,client)
        self._undo_service.record(Operation(function_undo,function_redo))

    def remove_client(self,client_id):
        """
        Removes a client
        :param client_id: the id of the client to be removed
        :return: None
        """
        # 1. remove client
        client=self._repo.remove(client_id)

        # 2. remove all rentals of this client
        rentals= self._rental_service.rentals()
        for rent in rentals:
            if rent.client_id==client_id:
                self._rental_service.remove_rental(rent.rental_id)


        function_undo=FunctionCall(self._repo.add,client)
        function_redo=FunctionCall(self._repo.remove,client_id)
        operations = [Operation(function_undo, function_redo)]
        #self._undo_service.record(Operation(function_undo,function_redo))

        rental_repo = self._rental_service.getRepo()
        for rental in rentals:
            if rental.client_id==client_id:
                function_undo = FunctionCall(rental_repo.add, rental)
                function_redo = FunctionCall(self._rental_service.remove_rental, rental.rental_id)
                operations.append(Operation(function_undo, function_redo))
        self._undo_service.record(CascadeOperation(*operations))
        return client

    def update_client(self,client_id,new_name):
        """
        Updates a client
        :param client_id: the id of the client to be updated
        :param new_name: the new name of the client
        :return: None
        """
        old_client=self._repo.search_id(client_id)
        self._repo.update(client_id,new_name)

        new_client=self._repo.search_id(client_id)

        function_undo=FunctionCall(self._repo.update,client_id,old_client.name)
        function_redo=FunctionCall(self._repo.update,client_id,new_client.name)
        self._undo_service.record(Operation(function_undo,function_redo))

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
