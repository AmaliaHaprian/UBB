from src.domain.client import Client
from src.repository.client_repository.client_memo_repo import ClientMemoRepo


class ClientTextRepo(ClientMemoRepo):
    def __init__(self, file_name='clients.txt'):
        super().__init__()
        self.file_name = file_name
        self._load()

    def _load(self):
        with open(self.file_name, 'rt') as fin:
            line = fin.readline()
            while line:
                current_line=line.split(",")
                if current_line[0]!="\n":
                    new_client=Client(int(current_line[0]), current_line[1])
                    super().add(new_client)
                line=fin.readline()
        fin.close()

    def _save(self):
        #fout=open(self._file_name, "wt")
        #for student in self.get_all():
        #    fout.write(student.to_str() + "\n")

        fout=open(self.file_name,"wt")
        for client in self.get_all():
            fout.write(str(client.client_id)+ "," +client.name +"\n")
        fout.close()

    def add(self, client):
        super().add(client)
        self._save()
    def remove(self, client):
        client=super().remove(client)
        self._save()
        return client
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

    #def __iter__(self):
     #   self._load()
      #  return super().__iter__()
    #def __getitem__(self, key):
     #   self._load()
      #  return super().__getitem__(key)