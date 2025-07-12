from src.domain.book import Book
from src.repository.book_repository.book_memo_repo import BookMemoRepo


class BookTextRepo(BookMemoRepo):

    def __init__(self, file_path):
        super().__init__()
        self._file_path=file_path
        self._file_loaded=False
        self._load()

    def _load(self):
        if self._file_loaded is True:
            return
        self._file_loaded=True
        with open(self._file_path, "rt") as fin:
            line = fin.readline()
            while line:
                tokens=line.split(",")
                if tokens[0]!="\n":
                    new_book=Book(int(tokens[0]), tokens[1], tokens[2])
                    super().add(new_book)
                line=fin.readline()
        fin.close()

    def _save(self):
        with open(self._file_path, "wt") as fout:
            for book in self._data.values():
                fout.write(str(book.book_id) + "," + book.title + "," + book.author + "\n")
        fout.close()

    def add(self, book):
        super().add(book)
        self._save()
    def remove(self, book):
        super().remove(book)
        self._save()
    def update(self, book_id, new_title, new_author):
        super().update(book_id, new_title, new_author)
        self._save()
    def get_all(self):
        return super().get_all()
    def search_by_id(self, book_id):
        return super().search_by_id(book_id)
    def search_by_title(self, book_title):
        return super().search_by_title(book_title)
    def search_by_author(self, book_author):
        return super().search_by_author(book_author)
    def get_id_from_title(self, book_title):
        return super().get_id_from_title(book_title)
    #def __iter__(self):
    #    self._load()
     #   return super().__iter__()
    #def __getitem__(self, key):
     #   self._load()
     #   return super().__getitem__(key)
if __name__ == "__main__":
    repo=BookTextRepo()
    repo.add(Book(1, "title","author"))
    print(len(repo.get_all()))

