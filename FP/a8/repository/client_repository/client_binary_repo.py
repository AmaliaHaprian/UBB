import pickle

from src.repository.client_repository.client_memo_repo import ClientMemoRepo


class ClientBinaryRepo(ClientMemoRepo):
    def __init__(self, file_name="clients.pickle"):
        super().__init__()
        self._file_name = file_name
        self._load()
    def _load(self):
        try:
            fin=open(self._file_name, "rb")
            text=pickle.load(fin)
        except EOFError:
            return
        for client in text:
            if client not in text:
                super().add(client)

    def _save(self):
        with open(self._file_name, "wb") as fout:
            pickle.dump(self, fout)

    def add(self, client):
        super().add(client)
        self._save()
    def remove(self, client):
        super().remove(client)
        self._save()
    def update(self, client_id, new_name):
        super().update(client_id, new_name)
        self._save()
    def get_last_client(self):
        return super().get_last_client()
    def get_all(self):
        return super().get_all()
    def search_by_client_id(self, client_id):
        return super().search_by_client_id(client_id)
    def search_by_name(self, name):
        return super().search_by_name(name)